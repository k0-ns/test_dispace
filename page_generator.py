def generate_page(otveti, background_image_url):
    PAGE = '''
    <head>
        <title>Мои курсы | eltex</title>
        <meta charset="UTF-8">
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
    </head>
    <body style="margin:0;height:100vh;background:url(''' + background_image_url + ''') center/cover fixed;">
        <a href="/seti/?next=1" 
           style="position:fixed;top:420px;right:400px;padding:5px;background:transparent;border:none;text-decoration:none;color:black;width:140px;height:150px"
        ></a>

        <textarea 
            id="dragBox"
            readonly 
            style="
                position: fixed;
                bottom: 20px;
                left: 20px;
                width: 300px;
                height: 75px;
                padding: 10px;
                font-size: 14px;
                resize: none;
                cursor: move;
                z-index: 1000;
                background: white;
                border: 1px solid #ccc;
            "
        >''' + otveti + '''</textarea>

        <script>
            const box = document.getElementById('dragBox');
            let dragging = false;
            let isSmall = false;
            
            box.onmousedown = function(e) {
                dragging = true;
                box.style.cursor = 'grabbing';
            };
            
            document.onmousemove = function(e) {
                if (!dragging) return;
                box.style.left = e.clientX - 150 + 'px';
                box.style.top = e.clientY - 37 + 'px';
                box.style.bottom = 'auto';
            };
            
            document.onmouseup = function() {
                dragging = false;
                box.style.cursor = 'move';
            };
            
            // Двойной клик - меняем размер
            box.ondblclick = function() {
                if (isSmall) {
                    // Возвращаем нормальный
                    box.style.width = '300px';
                    box.style.height = '75px';
                    box.style.fontSize = '14px';
                    box.style.padding = '10px';
                } else {
                    // Делаем очень маленькой
                    box.style.width = '50px';
                    box.style.height = '20px';
                    box.style.fontSize = '2px';
                    box.style.padding = '1px';
                }
                isSmall = !isSmall;
            };
        </script>
    </body>
    '''
    return PAGE