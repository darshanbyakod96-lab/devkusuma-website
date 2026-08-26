from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Devkusuma | Authentic Maharashtrian Restaurant</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: Georgia, serif;
            background: #fff8ed;
            color: #3a2114;
        }

        nav {
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 100;
            padding: 18px 7%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255,248,237,0.96);
        }

        .logo {
            font-size: 28px;
            font-weight: bold;
            color: #8b2f1c;
        }

        .logo span {
            display: block;
            font-family: Arial;
            font-size: 10px;
            letter-spacing: 3px;
            color: #9b6b32;
        }

        nav ul {
            display: flex;
            gap: 30px;
            list-style: none;
        }

        nav a {
            text-decoration: none;
            color: #3a2114;
            font-weight: bold;
        }

        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            padding: 120px 7%;
            color: white;

            background:
            linear-gradient(
                rgba(55,25,10,.68),
                rgba(55,25,10,.68)
            ),
            url("https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=1800&q=85")
            center/cover;
        }

        .hero-content {
            max-width: 750px;
        }

        .tag {
            display: inline-block;
            background: #e3a83b;
            color: #35170c;
            padding: 9px 18px;
            border-radius: 30px;
            font-family: Arial;
            font-size: 13px;
            font-weight: bold;
            margin-bottom: 25px;
        }

        h1 {
            font-size: clamp(55px, 8vw, 95px);
            line-height: .95;
            margin-bottom: 25px;
        }

        h1 span {
            color: #f1c05b;
        }

        .hero p {
            font-size: 20px;
            max-width: 620px;
            color: #f5e7d6;
            margin-bottom: 35px;
        }

        .buttons {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }

        .btn {
            padding: 14px 25px;
            border-radius: 30px;
            text-decoration: none;
            font-family: Arial;
            font-weight: bold;
        }

        .primary {
            background: #e3a83b;
            color: #35170c;
        }

        .secondary {
            border: 1px solid white;
            color: white;
        }

        section {
            padding: 90px 7%;
        }

        .section-title {
            text-align: center;
            margin-bottom: 50px;
        }

        .section-title small {
            font-family: Arial;
            color: #a83b20;
            letter-spacing: 3px;
            font-weight: bold;
        }

        .section-title h2 {
            font-size: 48px;
            margin-top: 8px;
        }

        .about {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: center;
        }

        .about-img {
            height: 500px;
            border-radius: 25px;

            background:
            url("https://images.unsplash.com/photo-1601050690117-94f5f6fa8bd7?auto=format&fit=crop&w=1000&q=85")
            center/cover;
        }

        .about-text h2 {
            font-size: 45px;
            margin-bottom: 20px;
        }

        .about-text p {
            color: #765d4d;
            font-size: 17px;
            margin-bottom: 18px;
        }

        .features {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 30px;
        }

        .feature {
            background: white;
            padding: 18px;
            border-radius: 15px;
            border: 1px solid #eadbc8;
        }

        .feature strong {
            display: block;
            color: #8b2f1c;
        }

        #dishes {
            background: #f4e5d0;
        }

        .dish-grid {
            display: grid;
            grid-template-columns: repeat(3,1fr);
            gap: 25px;
        }

        .dish {
            background: white;
            border-radius: 20px;
            overflow: hidden;
            transition: .3s;
        }

        .dish:hover {
            transform: translateY(-7px);
        }

        .dish-img {
            height: 220px;
            background-size: cover;
            background-position: center;
        }

        .dish-content {
            padding: 22px;
        }

        .dish-content h3 {
            font-size: 25px;
            margin-bottom: 7px;
        }

        .dish-content p {
            color: #806a5b;
        }

        .price {
            margin-top: 12px;
            color: #a83b20;
            font-family: Arial;
            font-weight: bold;
        }

        .menu {
            max-width: 900px;
            margin: auto;
        }

        .menu-item {
            display: flex;
            justify-content: space-between;
            padding: 22px 5px;
            border-bottom: 1px dashed #c9b49f;
        }

        .menu-item p {
            color: #806a5b;
            font-family: Arial;
            font-size: 13px;
        }

        .menu-price {
            color: #8b2f1c;
            font-weight: bold;
            white-space: nowrap;
        }

        #visit {
            background: #3d2014;
            color: white;
        }

        .info-grid {
            display: grid;
            grid-template-columns: repeat(3,1fr);
            gap: 30px;
        }

        .info-card {
            padding: 35px;
            border-radius: 20px;
            background: rgba(255,255,255,.05);
            border: 1px solid rgba(255,255,255,.15);
        }

        .info-card .icon {
            font-size: 35px;
        }

        .info-card h3 {
            color: #f1c05b;
            margin: 10px 0;
        }

        .info-card p {
            color: #e7d8ca;
        }

        .cta {
            text-align: center;
            background:
            linear-gradient(
                rgba(120,35,15,.88),
                rgba(120,35,15,.88)
            ),
            url("https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1600&q=80")
            center/cover;

            color: white;
        }

        .cta h2 {
            font-size: 50px;
            margin-bottom: 15px;
        }

        footer {
            background: #25130d;
            color: #d9c6b5;
            padding: 45px 7%;
            text-align: center;
        }

        footer h2 {
            color: white;
        }

        @media(max-width:850px) {

            nav ul {
                display: none;
            }

            .about {
                grid-template-columns: 1fr;
            }

            .dish-grid {
                grid-template-columns: 1fr;
            }

            .info-grid {
                grid-template-columns: 1fr;
            }

            .section-title h2 {
                font-size: 38px;
            }
        }

        @media(max-width:500px) {

            section {
                padding: 70px 5%;
            }

            .hero {
                padding: 120px 5% 70px;
            }

            h1 {
                font-size: 55px;
            }

            .features {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>

<nav>

    <div class="logo">
        Devkusuma
        <span>MAHARASHTRIAN RESTAURANT</span>
    </div>

    <ul>
        <li><a href="#about">About</a></li>
        <li><a href="#dishes">Specialities</a></li>
        <li><a href="#menu">Menu</a></li>
        <li><a href="#visit">Visit</a></li>
    </ul>

</nav>


<section class="hero">

    <div class="hero-content">

        <div class="tag">
            🌱 100% PURE VEGETARIAN
        </div>

        <h1>
            Taste the<br>
            <span>Heart of Maharashtra.</span>
        </h1>

        <p>
            Authentic Maharashtrian flavours, traditional recipes
            and comforting home-style food served with love in Wakad, Pune.
        </p>

        <div class="buttons">

            <a href="#menu" class="btn primary">
                Explore Menu
            </a>

            <a
                href="https://www.google.com/maps/search/?api=1&query=Devkusuma+Maharashtrian+Restaurant+Wakad+Pune"
                target="_blank"
                class="btn secondary">

                📍 Get Directions

            </a>

        </div>

    </div>

</section>


<section id="about">

    <div class="about">

        <div class="about-img"></div>

        <div class="about-text">

            <div class="section-title" style="text-align:left">

                <small>OUR STORY</small>

                <h2>
                    Gharacha Swad.<br>
                    Restaurant Madhye.
                </h2>

            </div>

            <p>
                Welcome to Devkusuma — a celebration of
                authentic Maharashtrian food and traditional flavours.
            </p>

            <p>
                From freshly prepared bhakri and pithla to
                delicious puran poli and crispy kothimbir wadi,
                every dish is inspired by the food we grew up loving.
            </p>

            <div class="features">

                <div class="feature">
                    <strong>🌱 Pure Vegetarian</strong>
                    100% vegetarian food
                </div>

                <div class="feature">
                    <strong>🏡 Home Style</strong>
                    Traditional recipes
                </div>

                <div class="feature">
                    <strong>🥘 Authentic</strong>
                    Maharashtrian flavours
                </div>

                <div class="feature">
                    <strong>❤️ Fresh</strong>
                    Prepared with care
                </div>

            </div>

        </div>

    </div>

</section>


<section id="dishes">

    <div class="section-title">

        <small>CUSTOMER FAVOURITES</small>

        <h2>Our Specialities</h2>

    </div>

    <div class="dish-grid">

        <div class="dish">

            <div
                class="dish-img"
                style="background-image:url('https://images.unsplash.com/photo-1626132647523-66f5bf380027?auto=format&fit=crop&w=900&q=80')">
            </div>

            <div class="dish-content">

                <h3>Puran Poli</h3>

                <p>
                    Soft traditional Maharashtrian sweet
                    flatbread filled with jaggery and dal.
                </p>

                <div class="price">
                    ₹199 / 2 pcs
                </div>

            </div>

        </div>


        <div class="dish">

            <div
                class="dish-img"
                style="background-image:url('https://images.unsplash.com/photo-1601050690117-94f5f6fa8bd7?auto=format&fit=crop&w=900&q=80')">
            </div>

            <div class="dish-content">

                <h3>Kothimbir Wadi</h3>

                <p>
                    Crispy coriander-based Maharashtrian
                    delicacy packed with flavour.
                </p>

            </div>

        </div>


        <div class="dish">

            <div
                class="dish-img"
                style="background-image:url('https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=900&q=80')">
            </div>

            <div class="dish-content">

                <h3>Thalipeeth</h3>

                <p>
                    Traditional multigrain Maharashtrian
                    flatbread with authentic spices.
                </p>

            </div>

        </div>

    </div>

</section>


<section id="menu">

    <div class="section-title">

        <small>FROM OUR KITCHEN</small>

        <h2>Popular Menu</h2>

    </div>

    <div class="menu">

        <div class="menu-item">
            <div>
                <h3>Mini Maharashtrian Thali</h3>
                <p>Compact traditional meal</p>
            </div>
            <div class="menu-price">₹169</div>
        </div>

        <div class="menu-item">
            <div>
                <h3>Regular Maharashtrian Thali</h3>
                <p>Wholesome traditional feast</p>
            </div>
            <div class="menu-price">₹349</div>
        </div>

        <div class="menu-item">
            <div>
                <h3>Maasvadi Thali</h3>
                <p>Maharashtrian speciality</p>
            </div>
            <div class="menu-price">₹399</div>
        </div>

        <div class="menu-item">
            <div>
                <h3>Pithla + Thecha + Jowari Bhakri</h3>
                <p>Classic Maharashtrian comfort food</p>
            </div>
            <div class="menu-price">₹259</div>
        </div>

        <div class="menu-item">
            <div>
                <h3>Varan Bhaat</h3>
                <p>Simple and comforting</p>
            </div>
            <div class="menu-price">₹249</div>
        </div>

        <div class="menu-item">
            <div>
                <h3>Akkhaa Masoor + Jowari Bhakri</h3>
                <p>Rich masoor preparation</p>
            </div>
            <div class="menu-price">₹259</div>
        </div>

        <div class="menu-item">
            <div>
                <h3>Puran Poli</h3>
                <p>Traditional Maharashtrian sweet</p>
            </div>
            <div class="menu-price">₹199 / 2</div>
        </div>

    </div>

</section>


<section id="visit">

    <div class="section-title">

        <small style="color:#f1c05b">
            COME VISIT US
        </small>

        <h2>Find Devkusuma</h2>

    </div>

    <div class="info-grid">

        <div class="info-card">

            <div class="icon">📍</div>

            <h3>Location</h3>

            <p>
                Shop No. 1, RGS Forte,<br>
                Bhumkar Das Gugre Road,<br>
                Bhagwan Nagar, Wakad,<br>
                Pimpri-Chinchwad, Pune.
            </p>

            <br>

            <a
                href="https://www.google.com/maps/search/?api=1&query=Devkusuma+Maharashtrian+Restaurant+Wakad+Pune"
                target="_blank"
                class="btn primary">

                Open Maps

            </a>

        </div>


        <div class="info-card">

            <div class="icon">🕐</div>

            <h3>Opening Hours</h3>

            <p>
                Thursday – Tuesday<br>
                11:00 AM – 4:00 PM<br>
                7:00 PM – 11:00 PM
            </p>

            <br>

            <p>
                Wednesday: Closed
            </p>

        </div>


        <div class="info-card">

            <div class="icon">💰</div>

            <h3>Average Cost</h3>

            <p>
                ₹200 – ₹400<br>
                for two people.
            </p>

            <br>

            <p>
                Traditional food at a
                budget-friendly price.
            </p>

        </div>

    </div>

</section>


<section class="cta">

    <h2>Ready for a Maharashtrian Feast?</h2>

    <p>
        Bring your family and enjoy the authentic taste of Maharashtra.
    </p>

    <div class="buttons" style="justify-content:center">

        <a href="#menu" class="btn primary">
            View Menu
        </a>

        <a
            href="https://www.google.com/maps/search/?api=1&query=Devkusuma+Maharashtrian+Restaurant+Wakad+Pune"
            target="_blank"
            class="btn secondary">

            Get Directions

        </a>

    </div>

</section>


<footer>

    <h2>Devkusuma</h2>

    <p>
        Authentic Maharashtrian Restaurant
        • 100% Pure Vegetarian
    </p>

    <br>

    <p>
        © 2026 Devkusuma. All rights reserved.
    </p>

</footer>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=True)
