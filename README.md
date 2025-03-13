## Running luminance.py with Pyodide

To run a Python script (luminance.py) in the browser using Pyodide, which packages the Python interpreter and its standard libraries into WebAssembly. The key steps are:

1. Place Pyodide’s .js and .wasm files (pyodide.js and pyodide.asm.wasm) in a directory accessible by web server.
In index.html, load Pyodide with a script tag：

![image](https://github.com/user-attachments/assets/0bbe2d50-21a0-4f8f-8b84-d509a3237298)

2. Fetch and run the Python script
After Pyodide is loaded, fetch luminance.py and pass it to pyodide.runPython():

The browser will download pyodide’s large .wasm file (embedding the Python interpreter), then executes luminance.py within that WebAssembly-compiled environment.

![image](https://github.com/user-attachments/assets/268498b5-ddf0-4e06-9920-9b8dfb808319)



## Problem facing

1. Pyodide includes the entire CPython interpreter and the Python standard library. This results in a .wasm file typically multiple megabytes in size.

![image](https://github.com/user-attachments/assets/d70f7507-7400-41ec-87b2-049b2a9fd355)

2. Not actually generate a wasm file for our environment to test with.


## Possible solution
For our targets like ESP32 and Renesas RISC‑V, using a minimal C/C++ or Rust codebase to rebuild the logic in Python and then compiled to WebAssembly seems to be a more feasible approach.
