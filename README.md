# Kuzu-Lab

[![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](http://kuzu-lab.netlify.app)

In-broswer Graph Analysis platform power by [kuzu_wasm](https://github.com/DylanShang/kuzu-wasm) and JupyterLite. This project aims to provide an easy-to-use interface for creating, analyzing, and visualizing graph data directly in the browser, with Python as the primary language for interacting with the graphs.



## ✨ Try it in your browser ✨

➡️ **http://kuzu-lab.netlify.app**

## Embedding into Quarto
Kuzu-Lab supports seamless embedding into Quarto documents, enabling interactive graph analysis in a variety of formats, from technical blogs to live code examples. We have developed a [Quarto Jupyter Console version](https://kuzu-lab.netlify.app/repl-example.html) , allowing users to run Python code directly within Quarto documents, bringing the power of graph analysis to an easily embeddable format.

Additionally, by integrating Quarto-live with PyVis, we've created [interactive web page](https://kuzu-lab.netlify.app/quarto-live.html) that allow users to visualize and interact with graphs in real-time. This is particularly well-suited for dynamic content in technical blogs or educational resources, providing an engaging way to showcase graph-related analyses.

## Requirements

JupyterLite is being tested against modern web browsers:

- Firefox 90+
- Chromium 89+


## Acknowledgments
- Kuzu Database System: Special thanks to the developers of the Kuzu database, whose work made this platform possible.
- JupyterLite: For enabling in-browser Jupyter-like experiences.
- Pyodide: For providing a full Python environment that runs in the browser, making Python-based graph analysis feasible in Kuzu-Lab.

## License
This project is licensed under the MIT License. 
