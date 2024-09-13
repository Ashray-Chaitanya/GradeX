document.getElementById('login-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            fetch('/home', {
                method: 'POST',
                body: formData
            }).then((response) => response.json()).then((data) => {
              if(data["error"]) {
                alert(data["error"]);
              }
              else {
                console.log(data);
                const anchor = document.createElement("a");
                anchor.style = "display:none";
                anchor.href = "/prof";
                anchor.click();
              }
            })
        });
