# Nand2Tetris Project 6: Hack Assembler

本專案為 [Nand2Tetris](https://www.nand2tetris.org/) 課程第六章（Project 6）的實作，使用 Python 撰寫的 **Hack 組譯器（Assembler）**。它能將 Hack 組合語言（`.asm`）編譯為 Hack 電腦架構可執行的 16-bit 二進位機器碼（`.hack`）。

## 檔案結構

```text
06/
├── assembler.py    # 組譯器主程式（包含 Parser, Code, SymbolTable 模組）
└── README.md       # 專案說明文件