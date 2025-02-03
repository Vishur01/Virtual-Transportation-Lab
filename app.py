from flask import Flask, render_template

app = Flask(__name__)



test_info = {
    'ctindex': {
        'title': 'CTindex Testing',
        'tests': {
            'ideal_ct': {
                'title': 'IDEAL-CT Test',
                'description': (
                    'An IDEAL-CT test was conducted to estimate the cracking resistance of a bituminous mixture '
                    'using DTS-30. It is similar to the traditional indirect tensile strength test. In this test, before '
                    'compaction, the laboratory-produced bituminous mixes underwent STOA. The STOA technique '
                    'follows the AASHTO R30 specification (Standard Practice for Mixture Conditioning of Hot Mix '
                    'Asphalt 2019) for mixture conditioning of performance samples, which includes 4 hours of loose '
                    'mixture aging at compaction temperature after mixing. '
                    '<br><br>'
                    'Following STOA, all tested mixes were compacted using the Marshall compactor at different '
                    'compactive level counts to simulate various stages of compaction and traffic. By evaluating '
                    'performance at different compactive efforts (35-110 blows, 7-2.5% air voids, respectively), we '
                    'aim to predict and optimize the long-term performance of the pavement.'
                )
            }
        },
        'image': 'static/ctindex.jpg'
    },
    'ps': {
        'title': 'Permanent Strain Testing',
        'description': (
                    'The dynamic creep test method determines the resistance to permanent deformation of the '
                    'bituminous mixture. The test was conducted at 60°C using Dynamic Testing System (DTS)-30 KN '
                    'as per BS EN 12597-25:2005. A short-term oven-aged (STOA) conditioned cylindrical specimen of '
                    'diameter 100 mm was used for the testing. Figure 2 shows the setup of the dynamic creep test. '
                    'The sample was subjected to a cyclic axial block-pulse loading with a frequency of 0.5 Hz and '
                    'stress of 100 kPa for 3600 repetitions. The cumulative axial strain εₙ in percent (%) after n load '
                    'applications can be calculated from the following equation: '
                    '<br><br>'
                    '<b>εₙ = cumulative axial strain of the specimen after n load applications, in percent (%);</b> '
                    '<br><b>hₒ = average height as measured by both displacement transducers after preloading of the specimen, '
                    'in millimeters (mm);</b> <br><b>hₙ = average height measured by both displacement transducers '
                    'after n load applications, in millimeters (mm).</b>'
                ),
        'image': 'static/its.jpg'
    },
    'its': {
        'title': 'ITS Testing',
        'description': (
            'ITS testing evaluates asphalt mixtures for tensile strength using indirect tensile methods. '
            '<br><br>'
            'The Modified Lottman test was conducted to evaluate the moisture sensitivity of the mix. The test involved '
            'the preparation of two subsets of the specimen: an unconditioned sample and a conditioned sample. '
            'The unconditioned samples were kept in a water bath for 2 hours at 25˚C, and after 2 hours, an Indirect '
            'Tensile Strength test was conducted. The load at which the specimen failed, referred to as Pdry, '
            'and ITSdry (kPa) can be calculated as follows (Equation 4):'
            '<br><br>'
            '<b>ITS<sub>dry</sub> = (2000 × P<sub>dry</sub>) / (π × t × D)</b> (Equation 4)'
            '<br><br>'
            'The conditioned samples were prepared by saturating the samples between 70%-80%, followed by freezing at '
            '-18˚C for 24 hours, then thawing at 60˚C for 24 hours, followed by 2 hours of conditioning in a water bath at 25˚C. '
            'Thereafter, an ITS test was conducted on this specimen, referred to as ITSwet, and can be calculated as follows (Equation 5):'
            '<br><br>'
            '<b>ITS<sub>wet</sub> = (2000 × P<sub>wet</sub>) / (π × t × D)</b> (Equation 5)'
            '<br><br>'
            'Where:'
            '<br><b>P</b> = Maximum load (N),'
            '<br><b>t</b> = Thickness of the sample (mm),'
            '<br><b>D</b> = Diameter of the sample (mm).'
            '<br><br>'
            'Dry ITS (unconditioned) and wet ITS (conditioned) were determined for calculating the Tensile Strength Ratio (TSR) '
            'of the mix using Equation 6:'
            '<br><br>'
            '<b>TSR = ITS<sub>wet</sub> / ITS<sub>dry</sub></b> (Equation 6)'
        ),
        'image': 'static/its.jpg'
    },
    'volumetric': {
        'title': 'Volumetric Testing',
        'description': 'Volumetric testing focuses on the spatial properties of asphalt mixtures.',
        'image': 'static/volumetric.jpg'
    }
}



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test-info/<test_type>')
def test_info_page(test_type):
    if test_type not in test_info:
        return 'Test type not found', 404
    return render_template('test_info.html', test_type=test_type, test_info=test_info)

if __name__ == "__main__":
    app.run(debug=True)
