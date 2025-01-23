from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IIT BHU Virtual Transportation Lab{% if test_type %} - {{ test_type|title }}{% endif %}</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --light-bg: #f8f9fa;
        }

        html, body {
            height: 100%;
            margin: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            line-height: 1.6;
            color: var(--primary-color);
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }

        .main-content {
            flex: 1 0 auto;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .top-bar {
            background-color: var(--primary-color);
            padding: 15px 20px;
            position: relative;
            display: flex;
            align-items: center;
        }

        .logo {
            height: 50px; /* Adjust the height as needed */
            margin-right: 20px; /* Space between logo and button */
        }

        .info-dropdown {
            position: relative;
            display: inline-block;
        }

        .info-btn {
            background-color: transparent;
            color: white;
            border: 2px solid white;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .info-btn:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: white;
            min-width: 200px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 4px;
            z-index: 1;
            margin-top: 5px;
        }

        .dropdown-content.show {
            display: block;
        }

        .test-category {
            padding: 12px 16px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .test-category:hover {
            background-color: var(--light-bg);
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }

        .service-card {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-decoration: none;
            color: var(--primary-color);
            transition: transform 0.2s;
        }

        .service-card:hover {
            transform: translateY(-5px);
        }

        .service-icon {
            font-size: 2.5em;
            color: var(--secondary-color);
            margin-bottom: 20px;
        }

        .service-title {
            font-size: 1.5em;
            font-weight: bold;
            margin-bottom: 15px;
        }

        .service-description {
            color: #666;
        }

        .test-info-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }

        .back-button {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--secondary-color);
            text-decoration: none;
            padding: 10px;
            margin-bottom: 20px;
        }

        .back-button:hover {
            color: var(--primary-color);
        }

        h1 {
            color: var(--primary-color);
            margin-bottom: 30px;
            text-align: center;
        }

        .test-info-section {
            margin-bottom: 30px;
            padding: 20px;
            background: var(--light-bg);
            border-radius: 10px;
            line-height: 1.6;
        }

        .test-info-section h2 {
            color: var(--secondary-color);
            margin-bottom: 15px;
            font-size: 1.5em;
        }

        .section-content {
            padding: 10px;
            background: white;
            border-radius: 8px;
            margin-top: 10px;
        }

        .footer {
            flex-shrink: 0;
            text-align: center;
            padding: 20px;
            background-color: var(--primary-color);
            color: white;
            width: 100%;
        }

        @media (max-width: 768px) {
            .services-grid {
                grid-template-columns: 1fr;
            }
            
            .container {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="main-content">
        {% if not test_type %}
        <!-- Home page content -->
        <div class="top-bar">
            <img src="{{ url_for('static', filename='logo.png') }}" alt="Logo" class="logo">
            <div class="info-dropdown">
                <button class="info-btn" onclick="toggleDropdown()">
                    <i class="fas fa-info-circle"></i> Test Information
                </button>
                <div class="dropdown-content" id="dropdown">
                    <div class="test-category" onclick="window.location.href='/test-info/ctindex'">
                        CTindex-PS <i class="fas fa-arrow-right"></i>
                    </div>
                    <div class="test-category" onclick="window.location.href='/test-info/its'">
                        ITS <i class="fas fa-arrow-right"></i>
                    </div>
                    <div class="test-category" onclick="window.location.href='/test-info/volumetric'">
                        Volumetric <i class="fas fa-arrow-right"></i>
                    </div>
                </div>
            </div>
        </div>

        <div class="container">
            <h1>IIT BHU Virtual Transportation Lab</h1>
            
            <div class="services-grid">
                <a href="https://lab-tester.onrender.com/" class="service-card">
                    <i class="fas fa-vial service-icon"></i>
                    <div class="service-title">CTindex-PS Testing</div>
                    <div class="service-description">
                        Advanced material cracking potential analysis using state-of-the-art testing methodologies.
                    </div>
                </a>

                <a href="https://its-sx5e.onrender.com/" class="service-card">
                    <i class="fas fa-compress-alt service-icon"></i>
                    <div class="service-title">ITS Analysis</div>
                    <div class="service-description">
                        Comprehensive indirect tensile strength testing for asphalt mixtures evaluation.
                    </div>
                </a>

                <a href="https://volumetrics.onrender.com/" class="service-card">
                    <i class="fas fa-cube service-icon"></i>
                    <div class="service-title">Volumetric Testing</div>
                    <div class="service-description">
                        Precise volumetric property assessment for optimal mixture design and quality control.
                    </div>
                </a>
            </div>
        </div>
        {% else %}
        <!-- Test info page content -->
        <div class="test-info-container">
            <a href="/" class="back-button">
                <i class="fas fa-arrow-left"></i> Back to Home
            </a>
            
            <h1>{{ test_type|title }} Testing Information</h1>
            
            <div class="test-info-section">
                <h2>Overview</h2>
                <div class="section-content">
                    {{ test_info[test_type]['overview'] }}
                </div>
            </div>

            <div class="test-info-section">
                <h2>Procedure</h2>
                <div class="section-content">
                    {{ test_info[test_type][' procedure'] }}
                </div>
            </div>

            <div class="test-info-section">
                <h2>Applications</h2>
                <div class="section-content">
                    {{ test_info[test_type]['applications'] }}
                </div>
            </div>
        </div>
        {% endif %}
    </div>

    <footer class="footer">
        <p>© 2024 IIT BHU Virtual Transportation Lab. All rights reserved.</p>
    </footer>

    <script>
        function toggleDropdown() {
            document.getElementById('dropdown').classList.toggle('show');
        }

        window.onclick = function(event) {
            if (!event.target.matches('.info-btn') && !event.target.closest('.dropdown-content')) {
                const dropdown = document.getElementById('dropdown');
                if (dropdown.classList.contains('show')) {
                    dropdown.classList.remove('show');
                }
            }
        }
    </script>
</body>
</html>
"""

# Test information dictionary
test_info = {
    'ctindex': {
        'overview': 'CTindex-PS is a specialized test that measures the cracking potential of materials through advanced analysis methods.',
        'procedure': 'The test involves preparing standardized specimens, conditioning them under controlled temperatures, and measuring their response to applied loads.',
        'applications': 'Commonly used in pavement design, material quality control, and research applications for predicting long-term performance.'
    },
    'its': {
        'overview': 'Indirect Tensile Strength (ITS) testing evaluates the tensile characteristics of asphalt mixtures.',
        'procedure': 'Specimens are loaded diametrically at a controlled rate until failure, measuring the maximum load and deformation.',
        'applications': 'Used for mix design validation, quality control, and performance prediction in road construction.'
    },
    'volumetric': {
        'overview': 'Volumetric testing analyzes the spatial composition and properties of asphalt mixtures.',
        'procedure': 'Involves measuring bulk specific gravity, maximum specific gravity, and calculating air void content.',
        'applications': 'Essential for mix design optimization, quality assurance, and conformance to specifications.'
    }
}

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/test-info/<test_type>')
def test_info_page(test_type):
    if test_type not in test_info:
        return 'Test type not found', 404
    return render_template_string(
        html_template,
        test_type=test_type,
        test_info=test_info
    )

if __name__ == "__main__":
    app.run(debug=True)