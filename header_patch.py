        with gr.Box(visible=is_spaces):
            if(is_spaces and is_shared_ui):
                gr.HTML(f'''
                <div class="gr-prose" style="max-width: 80%">
                    <p>🚨 We have a new version ✨ please try it and add a comment if you find any issues. <a style="color: #00ff00;" href="https://huggingface.co/spaces/camenduru/webui-docker">https://huggingface.co/spaces/camenduru/webui-docker</a></p>
                    <br>
                    <p>🚧 (WIP) Automatic1111 Stable Diffusion Web UI on 🤗 Hugging Face Spaces | Running model: Linaqruf/anything-v3.0</p>
                    <p>You can duplicate this Space to run it privately without a queue and load additional checkpoints.&nbsp;&nbsp;<a class="duplicate-button" style="display:inline-block" target="_blank" href="https://huggingface.co/spaces/{os.environ['SPACE_ID']}?duplicate=true"><img style="margin: 0" src="https://img.shields.io/badge/-Duplicate%20Space-blue?labelColor=white&style=flat&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAP5JREFUOE+lk7FqAkEURY+ltunEgFXS2sZGIbXfEPdLlnxJyDdYB62sbbUKpLbVNhyYFzbrrA74YJlh9r079973psed0cvUD4A+4HoCjsA85X0Dfn/RBLBgBDxnQPfAEJgBY+A9gALA4tcbamSzS4xq4FOQAJgCDwV2CPKV8tZAJcAjMMkUe1vX+U+SMhfAJEHasQIWmXNN3abzDwHUrgcRGmYcgKe0bxrblHEB4E/pndMazNpSZGcsZdBlYJcEL9Afo75molJyM2FxmPgmgPqlWNLGfwZGG6UiyEvLzHYDmoPkDDiNm9JR9uboiONcBXrpY1qmgs21x1QwyZcpvxt9NS09PlsPAAAAAElFTkSuQmCC&logoWidth=14" alt="Duplicate Space"></a> <a style="display:inline-block" href="https://github.com/camenduru/stable-diffusion-webui-colab" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a></p> 
                    <p>📝 How to add private model or embed? 📺 Tutorial Video: <a href="https://youtu.be/jpxWRMino6c" style="target=" _blank"="">https://youtu.be/jpxWRMino6c</a> 🐣 Please follow me for new updates <a href="https://twitter.com/camenduru" style="target=" _blank"="">https://twitter.com/camenduru</a> </p>
                </div>
                ''')
            elif(is_spaces):
                import torch
                if(not torch.cuda.is_available()):
                    gr.HTML(f'''
                    <div class="gr-prose" style="max-width: 80%">
                        <p>🚧 (WIP) Private Automatic1111 Stable Diffusion Web UI on 🤗 Hugging Face Spaces</p>
                        <p>This Space is currently running on CPU, this WebUI may not run on CPU 🥶, you can upgrade for a GPU <a href="https://huggingface.co/spaces/{os.environ['SPACE_ID']}/settings" style="text-decoration: underline" target="_blank">in the Settings tab</a> <a style="display:inline-block" href="https://github.com/camenduru/stable-diffusion-webui-colab" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a></p> 
                        <p>📝 How to add private model or embed? 📺 Tutorial Video: <a href="https://youtu.be/jpxWRMino6c" style="target=" _blank"="">https://youtu.be/jpxWRMino6c</a> 🐣 Please follow me for new updates <a href="https://twitter.com/camenduru" style="target=" _blank"="">https://twitter.com/camenduru</a> </p>
                    </div>
                ''')
                else:
                    gr.HTML(f'''
                    <div class="gr-prose" style="max-width: 80%">
                        <p>🚧 (WIP) Private Automatic1111 Stable Diffusion Web UI on 🤗 Hugging Face Spaces</p>
                        <p>It is running on a GPU 🔥, you can <a href="https://huggingface.co/spaces/{os.environ['SPACE_ID']}/settings" style="text-decoration: underline" target="_blank">don't forget to remove the GPU attribution</a> once your are done playing with it <a style="display:inline-block" href="https://github.com/camenduru/stable-diffusion-webui-colab" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a></p> 
                        <p>📝 How to add private model or embed? 📺 Tutorial Video: <a href="https://youtu.be/jpxWRMino6c" style="target=" _blank"="">https://youtu.be/jpxWRMino6c</a> 🐣 Please follow me for new updates <a href="https://twitter.com/camenduru" style="target=" _blank"="">https://twitter.com/camenduru</a> </p>
                    </div>
                ''')
