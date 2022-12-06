        with gr.Box(visible=is_spaces):
            if(is_spaces and is_shared_ui):
                gr.HTML(f'''
                <div class="gr-prose" style="max-width: 80%">
                    <h2>Automatic1111 Stable Diffusion WebUI on Hugging Face Spaces 🎨 Running model: Linaqruf/anything-v3.0</h2>
                    <p>You can duplicate this Space to run it privately without a queue and load additional checkpoints.&nbsp;&nbsp;<a class="duplicate-button" style="display:inline-block" target="_blank" href="https://huggingface.co/spaces/{os.environ['SPACE_ID']}?duplicate=true"><img style="margin: 0" src="https://img.shields.io/badge/-Duplicate%20Space-blue?labelColor=white&style=flat&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAP5JREFUOE+lk7FqAkEURY+ltunEgFXS2sZGIbXfEPdLlnxJyDdYB62sbbUKpLbVNhyYFzbrrA74YJlh9r079973psed0cvUD4A+4HoCjsA85X0Dfn/RBLBgBDxnQPfAEJgBY+A9gALA4tcbamSzS4xq4FOQAJgCDwV2CPKV8tZAJcAjMMkUe1vX+U+SMhfAJEHasQIWmXNN3abzDwHUrgcRGmYcgKe0bxrblHEB4E/pndMazNpSZGcsZdBlYJcEL9Afo75molJyM2FxmPgmgPqlWNLGfwZGG6UiyEvLzHYDmoPkDDiNm9JR9uboiONcBXrpY1qmgs21x1QwyZcpvxt9NS09PlsPAAAAAElFTkSuQmCC&logoWidth=14" alt="Duplicate Space"></a></p> 
                </div>
                ''')
            elif(is_spaces):
                import torch
                if(not torch.cuda.is_available()):
                    gr.HTML(f'''
                    <div class="gr-prose" style="max-width: 80%">
                        <h2>Private Automatic1111 Stable Diffusion WebUI on Hugging Face Spaces 🎨</h2>
                        <p>This Space is currently running on CPU, this WebUI may not run on CPU 🥶, you can upgrade for a GPU <a href="https://huggingface.co/spaces/{os.environ['SPACE_ID']}/settings" style="text-decoration: underline" target="_blank">in the Settings tab</a></p> 
                    </div>
                ''')
                else:
                    gr.HTML(f'''
                    <div class="gr-prose" style="max-width: 80%">
                        <h2>Private Automatic1111 Stable Diffusion WebUI on Hugging Face Spaces 🎨</h2>
                        <p>It is running on a GPU 🔥, you can <a href="https://huggingface.co/spaces/{os.environ['SPACE_ID']}/settings" style="text-decoration: underline" target="_blank">don't forget to remove the GPU attribution</a> once your are done playing with it</p> 
                    </div>
                ''')
