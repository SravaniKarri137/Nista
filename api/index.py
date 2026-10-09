
from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#fff1f7">
<title>For Nishta Didi 💗</title>

<style>
* {
    box-sizing: border-box;
}

:root {
    --pink: #f5a6c1;
    --deep: #a13f6b;
    --text: #634558;
    --paper: #fffafc;
}

body {
    margin: 0;
    min-height: 100vh;
    padding: 28px 16px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Georgia, "Times New Roman", serif;
    color: var(--text);
    background:
        radial-gradient(circle at 10% 10%, #ffe1ed, transparent 35%),
        radial-gradient(circle at 90% 90%, #e8ddff, transparent 35%),
        linear-gradient(135deg, #fff8fb, #f9f2ff);
}

.container {
    width: 100%;
    max-width: 620px;
    text-align: center;
}

.eyebrow {
    font-family: Arial, sans-serif;
    font-size: 11px;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #ad7390;
    margin-bottom: 14px;
}

h1 {
    color: var(--deep);
    font-weight: normal;
    font-size: clamp(34px, 8vw, 48px);
    margin: 0 0 12px;
}

.subtitle {
    color: #8b6b80;
    line-height: 1.8;
    font-size: 16px;
    margin: 0 auto 28px;
    max-width: 420px;
}

.envelope-area {
    display: flex;
    justify-content: center;
    margin: 30px auto 20px;
}

.envelope {
    position: relative;
    width: min(330px, 86vw);
    height: 205px;
    background: #f4b3ca;
    border-radius: 8px;
    box-shadow: 0 18px 45px #a94e7425;
    cursor: pointer;
    transition: transform 0.3s ease;
}

.envelope:hover {
    transform: translateY(-4px);
}

.envelope-back {
    position: absolute;
    inset: 0;
    background: #f8c7d9;
    border-radius: 8px;
}

.envelope-flap {
    position: absolute;
    inset: 0;
    background: #ee9fbc;
    clip-path: polygon(0 0, 100% 0, 50% 58%);
    transform-origin: top;
    transition: transform 0.8s ease, opacity 0.5s ease;
    z-index: 4;
}

.envelope-front {
    position: absolute;
    inset: 0;
    background: #f9c4d7;
    clip-path: polygon(0 100%, 0 0, 50% 55%, 100% 0, 100% 100%);
    z-index: 3;
}

.envelope-seal {
    position: absolute;
    top: 78px;
    left: 50%;
    transform: translateX(-50%);
    width: 44px;
    height: 44px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 23px;
    background: #fff5f8;
    box-shadow: 0 3px 12px #a13f6b20;
    z-index: 5;
    transition: opacity 0.3s ease;
}

.envelope-label {
    position: absolute;
    bottom: 19px;
    left: 0;
    right: 0;
    color: #914d6b;
    font-family: Arial, sans-serif;
    font-size: 12px;
    letter-spacing: 1px;
    z-index: 6;
}

.open-hint {
    color: #a16f88;
    font-family: Arial, sans-serif;
    font-size: 13px;
    margin-bottom: 28px;
}

.letter {
    display: none;
    background: var(--paper);
    border: 1px solid #f1d6e2;
    border-radius: 18px;
    padding: clamp(22px, 6vw, 42px);
    text-align: left;
    box-shadow: 0 18px 55px #9d52751a;
    animation: appear 1s ease both;
}

.letter.show {
    display: block;
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.letter-heading {
    text-align: center;
    color: var(--deep);
    font-size: 29px;
    font-weight: normal;
    margin: 0 0 24px;
}

.letter p {
    font-size: 16px;
    line-height: 1.95;
    margin: 0 0 17px;
}

.signature {
    color: var(--deep);
    font-size: 21px;
    line-height: 1.8;
    margin-top: 25px;
}

.divider {
    height: 1px;
    background: linear-gradient(to right, transparent, #e8b7cb, transparent);
    margin: 27px 0;
}

.surprise {
    display: none;
    margin-top: 24px;
    text-align: center;
    padding: 23px 15px;
    border-radius: 14px;
    background: linear-gradient(135deg, #fff0f6, #f3edff);
    animation: appear 1s ease both;
}

.surprise.show {
    display: block;
}

.surprise-label {
    font-family: Arial, sans-serif;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #a16c88;
    margin-bottom: 12px;
}

.surprise h2 {
    font-size: 27px;
    font-weight: normal;
    color: var(--deep);
    margin: 0 0 12px;
}

.surprise p {
    margin-bottom: 0;
    text-align: center;
    line-height: 1.8;
}

.footer {
    color: #a77c93;
    font-size: 12px;
    margin-top: 28px;
    font-family: Arial, sans-serif;
}

.floating {
    position: fixed;
    bottom: -35px;
    pointer-events: none;
    animation: floatUp 6s ease-in forwards;
    z-index: 10;
}

@keyframes floatUp {
    0% {
        opacity: 0;
        transform: translateY(0) rotate(0);
    }
    15% {
        opacity: 0.8;
    }
    100% {
        opacity: 0;
        transform: translateY(-110vh) rotate(35deg);
    }
}

@media (max-width: 420px) {
    body {
        padding: 22px 13px;
    }

    .letter p {
        font-size: 15px;
        line-height: 1.85;
    }

    .envelope {
        height: 185px;
    }

    .envelope-seal {
        top: 68px;
    }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
</style>
</head>

<body>

<audio id="music" loop preload="auto">
    <source src="/static/maahi_ve.mp3" type="audio/mpeg">
</audio>

<main class="container">

    <div class="eyebrow">A little something, just for you</div>

    <h1>For Nishta Didi 💗</h1>

    <p class="subtitle">
        Some people become a part of our everyday life
        before we realise how much they mean to us.
        This little letter is for one of those people.
    </p>

    <section id="envelopeArea">
        <div class="envelope-area">
            <div class="envelope" id="envelope"
                 role="button" tabindex="0"
                 aria-label="Open your farewell letter">

                <div class="envelope-back"></div>
                <div class="envelope-flap" id="flap"></div>
                <div class="envelope-front"></div>

                <div class="envelope-seal" id="seal">♡</div>

                <div class="envelope-label">
                    TO MY DEAR NISTA DIDI
                </div>
            </div>
        </div>

        <div class="open-hint">Tap the envelope to open your letter ♡</div>
    </section>

    <article class="letter" id="letter">

        <h2 class="letter-heading">Dear Nishta Didi, ♡</h2>

        <p>
            It's crazy to think that you came here so unexpectedly,
            just for two months, and somehow became so familiar in
            such a short time.
        </p>

        <p>
            I never imagined I'd get this used to having you around.
            It's funny how someone can enter your life unexpectedly
            and become a part of your everyday routine before you
            even realise it.
        </p>

        <p>
            I'll miss our little conversations, the random moments,
            and simply having you around. Honestly, I wish these
            two months had been a little longer. 🥹💗
        </p>

        <p>
            I'm really glad life brought you here, Didi. You may
            have come as a temporary roommate, but you'll always
            be a lovely part of my memories.
        </p>

        <p>
            Go home happily, take care of yourself, and don't forget
            me! I hope we stay in touch and never become strangers
            just because we're no longer sharing the same space.
        </p>

        <p>
            <strong>
                Two months were short, but I'm so glad they had
                you in them. ♡
            </strong>
        </p>

        <div class="signature">
            With lots of love,<br>
            Your roommate 💗
        </div>

        <div class="divider"></div>

        <section class="surprise" id="surprise">
            <div class="surprise-label">One last little thing</div>

            <h2>You'll be missed, Didi. ♡</h2>

            <p>
                You came here unexpectedly, stayed for just two months,
                and somehow made saying goodbye harder than I imagined.
                <br><br>
                <strong>Once my roommate, always my Didi. 💗</strong>
            </p>
        </section>

    </article>

    <div class="footer">
        Made with love, for a memory that stays. ♡
    </div>

</main>

<script>
const audio = document.getElementById("music");
const envelope = document.getElementById("envelope");
const flap = document.getElementById("flap");
const seal = document.getElementById("seal");
const envelopeArea = document.getElementById("envelopeArea");
const letter = document.getElementById("letter");
const surprise = document.getElementById("surprise");

let opened = false;

// Attempt autoplay. Mobile browsers may block this until a tap.
function startMusic() {
    audio.play().catch(() => {
        // Music will be retried when the envelope is tapped.
    });
}

startMusic();

async function openLetter() {
    if (opened) return;
    opened = true;

    // Play the song directly from the envelope tap.
    try {
        await audio.play();
    } catch (error) {
        console.log("Music could not start:", error);
    }

    flap.style.transform = "rotateX(180deg)";
    flap.style.opacity = "0";
    seal.style.opacity = "0";

    setTimeout(() => {
        envelopeArea.style.display = "none";
        letter.classList.add("show");

        setTimeout(() => {
            surprise.classList.add("show");
            floatDecorations();
        }, 1800);
    }, 650);
}

function floatDecorations() {
    const symbols = ["♡", "✧", "♥", "✦"];

    for (let i = 0; i < 16; i++) {
        setTimeout(() => {
            const item = document.createElement("span");
            item.className = "floating";
            item.textContent = symbols[
                Math.floor(Math.random() * symbols.length)
            ];

            item.style.left = Math.random() * 100 + "vw";
            item.style.fontSize = (14 + Math.random() * 15) + "px";
            item.style.color =
                Math.random() > 0.5 ? "#e58eaf" : "#b6a0e8";
            item.style.animationDuration = (4 + Math.random() * 3) + "s";

            document.body.appendChild(item);

            setTimeout(() => item.remove(), 7500);
        }, i * 160);
    }
}

envelope.addEventListener("click", openLetter);

envelope.addEventListener("keydown", function(event) {
    if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        openLetter();
    }
});
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(PAGE)


if __name__ == "__main__":
    app.run(debug=True)
