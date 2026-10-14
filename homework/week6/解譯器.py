import re

class Term:
    pass

class Var(Term):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class Abs(Term):
    def __init__(self, param, body):
        self.param = param  # 參數名稱 (字串)
        self.body = body    # 本體 (Term)
    def __repr__(self):
        return f"(\\{self.param}. {self.body})"

class App(Term):
    def __init__(self, func, arg):
        self.func = func    # 函數 (Term)
        self.arg = arg      # 參數 (Term)
    def __repr__(self):
        return f"({self.func} {self.arg})"

def free_vars(term):
    if isinstance(term, Var):
        return {term.name}
    elif isinstance(term, Abs):
        return free_vars(term.body) - {term.param}
    elif isinstance(term, App):
        return free_vars(term.func) | free_vars(term.arg)

def substitute(term, var_name, replacement):
    """將 term 中所有自由的 var_name 取代為 replacement（包含基本的 Alpha 轉換防護）"""
    if isinstance(term, Var):
        return replacement if term.name == var_name else term
    elif isinstance(term, Abs):
        if term.param == var_name:
            return term  # 變數已被遮蔽 (shadowed)
        elif term.param in free_vars(replacement):
            # 避免變數捕捉，進行重新命名 (Alpha 轉換)
            new_param = term.param + "'"
            new_body = substitute(term.body, term.param, Var(new_param))
            return Abs(new_param, substitute(new_body, var_name, replacement))
        else:
            return Abs(term.param, substitute(term.body, var_name, replacement))
    elif isinstance(term, App):
        return App(substitute(term.func, var_name, replacement), substitute(term.arg, var_name, replacement))

def parse_tokens(tokens):
    if not tokens:
        raise SyntaxError("未預期的表達式結尾")
    
    token = tokens.pop(0)
    if token == '\\':
        if not tokens:
            raise SyntaxError("Lambda 抽象缺少參數名稱")
        param = tokens.pop(0)
        dot = tokens.pop(0)
        if dot != '.':
            raise SyntaxError(f"預期 '.' 但得到 '{dot}'")
        body = parse_tokens(tokens)
        return Abs(param, body)
    elif token == '(':
        # 解析函數與參數
        func = parse_tokens(tokens)
        arg = parse_tokens(tokens)
        close = tokens.pop(0)
        if close != ')':
            raise SyntaxError(f"預期 ')' 但得到 '{close}'")
        return App(func, arg)
    else:
        return Var(token)

def parse(expr_str):
    # 使用正規表達式進行詞法分析 (Lexer)
    tokens = re.findall(r'\\|\.|\(|\)|\w+', expr_str)
    return parse_tokens(tokens)

def evaluate(term, step=1):
    print(f"  [步驟 {step}] {term}")
    
    if isinstance(term, App):
        # 1. 若函數部分不是抽象，先化簡函數
        if not isinstance(term.func, Abs):
            new_func = evaluate(term.func, step)
            if new_func != term.func:
                return evaluate(App(new_func, term.arg), step + 1)
        
        # 2. 若函數是抽象，則執行 Beta-Reduction
        if isinstance(term.func, Abs):
            abs_term = term.func
            redex_result = substitute(abs_term.body, abs_term.param, term.arg)
            print(f"    -> 執行 Beta-Reduction: 將 \\{abs_term.param} 取代為 {term.arg}")
            return evaluate(redex_result, step + 1)
            
        # 3. 否則化簡參數部分
        new_arg = evaluate(term.arg, step)
        if new_arg != term.arg:
            return evaluate(App(term.func, new_arg), step + 1)
            
    elif isinstance(term, Abs):
        new_body = evaluate(term.body, step)
        if new_body != term.body:
            return Abs(term.param, new_body)
            
    return term

if __name__ == "__main__":
    print("=== Lambda Calculus 完整解譯器測試 ===\n")
    
    # 測試項目：計算 NOT(True)
    # 說明：
    #   True = \t. \f. t
    #   False = \t. \f. f
    #   NOT  = \p. ((p False) True) 
    #        = \p. ((p (\t. \f. f)) (\t. \f. t))
    #   運算式: (NOT True)
    
    expr_str = "((\\p. ((p (\\t. \\f. f)) (\\t. \\f. t))) (\\t. \\f. t))"
    
    print(f"輸入的 Lambda 表達式: {expr_str}")
    print("對應含意: NOT (True)\n")
    print("開始計算過程 (Evaluation Trace):")
    
    ast = parse(expr_str)
    final_result = evaluate(ast)
    
    print(f"\n最終計算結果: {final_result}")
    print("（註：結果 \\t. \\f. f 代表 Church 編碼中的 False）")