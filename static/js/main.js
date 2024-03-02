// static/js/main.js
async function generateText() {
    const inputText = document.getElementById('inputText').value;

    const response = await fetch('/generate_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `input_text=${encodeURIComponent(inputText)}`,
    });

    const result = await response.text();
    document.getElementById('output').innerHTML = result;
}

