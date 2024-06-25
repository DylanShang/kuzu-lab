import js
async def init() -> object:
    # import pyodide_js
    #load pyarrow
    # await pyodide_js.loadPackage("https://storage.googleapis.com/ibis-wasm-wheels/pyarrow-16.0.0.dev2661%2Bg9bddb87fd-cp311-cp311-emscripten_3_1_46_wasm32.whl")
    js_function = js.Function('obj', '''
        async function connectKuzu() {
                const baseUrl = "https://kuzu-lab.netlify.app";
                const wasmUrl = `${baseUrl}/package/dist/kuzu.js`;
                const kuzu_wasm = await import(wasmUrl)
                const kuzu = await kuzu_wasm.default();
                kuzu.FS.mkdir("data")
                return kuzu;
            }
        return connectKuzu()
    ''')
    js_obj = js.Object()
    # global kuzu 
    kuzu = await js_function(js_obj)

    def upload(filepath):
        import os,hashlib
        def encode_path_to_filename(file_path):
            # use SHA-256 encode
            encoded_path = hashlib.sha256(file_path.encode()).hexdigest()
            # get extension name
            file_extension = os.path.splitext(file_path)[1]
            # generate new filename
            new_file_name = f"{encoded_path}{file_extension}"
            return new_file_name
        target_filepath = "/data/" + encode_path_to_filename(filepath)
        try:
            with open(filepath,"r") as f:
                content = f.read()
                kuzu.FS.writeFile(target_filepath, content);
                return target_filepath
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            return False
        except IOError:
            print(f"Error: An I/O error occurred while reading the file '{file_path}'.")
            return False
    kuzu.upload = upload

    # def read(filepath):
    #     data_list = list(kuzu.FS.readFile("/data/user.csv"))
    #     byte_data = bytes(int_list)
    #     return byte_data.decode('utf-8')
    # kuzu.FS.read = read
    return kuzu


