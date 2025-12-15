document.addEventListener('DOMContentLoaded', () => {
    console.log('DS Navigator Website Loaded Successfully! Interactive features enabled.');

    const cards = document.querySelectorAll('.algorithm-card, .accordion-item');

    const fadeInObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px' 
    });

    cards.forEach(card => {
        card.style.opacity = 0;
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
 
        fadeInObserver.observe(card);
    });
});

function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
        throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

function runPython(codeId) {
    var code = document.getElementById(codeId).innerText;

    var outputElement = document.getElementById("consoleOutput");

    outputElement.innerText = ""; 
    outputElement.classList.remove("text-danger");
    outputElement.classList.add("text-success");

    if (typeof bootstrap !== 'undefined') {
        var outputModal = new bootstrap.Modal(document.getElementById('outputModal'));
        outputModal.show();
    } else {
        alert("Bootstrap library not loaded properly. Cannot show output.");
        return;
    }

    Sk.pre = "consoleOutput";
    Sk.configure({
        output: function(text) {
            outputElement.innerText += text;
        },
        read: builtinRead
    });

    var myPromise = Sk.misceval.asyncToPromise(function() {
        return Sk.importMainWithBody("<stdin>", false, code, true);
    });

    myPromise.then(function(mod) {
        console.log('Python code execution success');
    },
    function(err) {
        outputElement.innerText += "\n\n--- EXECUTION ERROR ---\n" + err.toString();
        outputElement.classList.add("text-danger"); 
        outputElement.classList.remove("text-success");
    });
}
