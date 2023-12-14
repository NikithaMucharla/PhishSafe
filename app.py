#importing required libraries
# import unittest
from flask import Flask, request, render_template, send_from_directory, url_for, redirect
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

file = open("pickle/model.pkl","rb")
gbc = pickle.load(file)
file.close()


app = Flask(__name__)

# Templates
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog1')
def blog1():
    return render_template('blog1.html')

@app.route('/blog2')
def blog2():
    return render_template('blog2.html')

@app.route('/blog3')
def blog3():
    return render_template('blog3.html')

@app.route('/blog4')
def blog4():
    return render_template('blog4.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/ev')
def ev():
    return render_template('ev.html')

@app.route("/phishing", methods=["GET", "POST"])
def phishing():
    if request.method == "POST":

        url = request.form["url"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30) 

        y_pred =gbc.predict(x)[0]
        #1 is safe       
        #-1 is unsafe
        y_pro_phishing = gbc.predict_proba(x)[0,0]
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        # if(y_pred ==1 ):
        pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)
        return render_template('phishing.html',xx =round(y_pro_non_phishing,2),url=url )
    return render_template('phishing.html', xx =-1)


@app.route('/pp')
def pp():
    return render_template('pp.html')

@app.route('/quiz1')
def quiz1():
    return render_template('quiz1.html')

@app.route('/quiz2')
def quiz2():
    return render_template('quiz2.html')

@app.route('/quiz3')
def quiz3():
    return render_template('quiz3.html')

@app.route('/quiz4')
def quiz4():
    return render_template('quiz4.html')

@app.route('/quiz5')
def quiz5():
    return render_template('quiz5.html')

@app.route('/quiz6')
def quiz6():
    return render_template('quiz6.html')

@app.route('/quizzes')
def quizzes():
    return render_template('quizzes.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/tos')
def tos():
    return render_template('tos.html')
# Templates -end
# assets
# css
@app.route('/assets/css/style.css')
def send_css():
    return send_from_directory('assets/css', 'style.css')
# css -end
# img
# blog -img
@app.route('/assets/img/blog/1.png')
def send_1_img():
    return send_from_directory('assets/img/blog', '1.png')

@app.route('/assets/img/blog/2.jpg')
def send_2_img():
    return send_from_directory('assets/img/blog', '2.jpg')

@app.route('/assets/img/blog/3.png')
def send_3_img():
    return send_from_directory('assets/img/blog', '3.png')

@app.route('/assets/img/blog/4.avif')
def send_4_img():
    return send_from_directory('assets/img/blog', '4.avif')

@app.route('/assets/img/blog/5.webp')
def send_5_img():
    return send_from_directory('assets/img/blog', '5.webp')

@app.route('/assets/img/blog/blog-2.jpg')
def send_blog2_img():
    return send_from_directory('assets/img/blog', 'blog-2.jpg')

@app.route('/assets/img/blog/blog-3.jpg')
def send_blog3_img():
    return send_from_directory('assets/img/blog', 'blog-3.jpg')

@app.route('/assets/img/blog/blog-4.jpg')
def send_blog4_img():
    return send_from_directory('assets/img/blog', 'blog-4.jpg')

@app.route('/assets/img/blog/blog-author.jpg')
def send_blog_author_img():
    return send_from_directory('assets/img/blog', 'blog-author.jpg')

@app.route('/assets/img/blog/blog1.png')
def send_blog1_img():
    return send_from_directory('assets/img/blog', 'blog1.png')

@app.route('/assets/img/blog/blog3.png')
def send_blog3i_img():
    return send_from_directory('assets/img/blog', 'blog3.png')

@app.route('/assets/img/blog/blog4.png')
def send_blog4i_img():
    return send_from_directory('assets/img/blog', 'blog4.png')

@app.route('/assets/img/blog/blog5.png')
def send_blog5_img():
    return send_from_directory('assets/img/blog', 'blog5.png')

@app.route('/assets/img/blog/Phishing-email-example-1024x772.jpeg')
def send_Phishing_email_img():
    return send_from_directory('assets/img/blog', 'Phishing-email-example-1024x772.jpeg-example-1024x772.jpeg')

@app.route('/assets/img/blog/xyz.png')
def send_xyz_img():
    return send_from_directory('assets/img/blog', 'xyz.png')
# blog -img -end
# team -img
@app.route('/assets/img/team/nikitha.jpg')
def send_nikitha_img():
    return send_from_directory('assets/img/team', 'nikitha.jpg')

@app.route('/assets/img/team/nisha.jpg')
def send_nisha_img():
    return send_from_directory('assets/img/team', 'nisha.jpg')

@app.route('/assets/img/team/hemanth.jpg')
def send_hemanth_img():
    return send_from_directory('assets/img/team', 'hemanth.jpg')

@app.route('/assets/img/team/chnadrashekhar.jpg')
def send_chnadrashekhar_img():
    return send_from_directory('assets/img/team', 'chnadrashekhar.jpg')

# team -img -end
@app.route('/assets/img/about.jpg')
def send_about_img():
    return send_from_directory('assets/img', 'about.jpg')

@app.route('/assets/img/features-2.png')
def send_features2_img():
    return send_from_directory('assets/img', 'features-2.png')

@app.route('/assets/img/features-3.png')
def send_features3_img():
    return send_from_directory('assets/img', 'features-3.png')

@app.route('/assets/img/features.png')
def send_features_img():
    return send_from_directory('assets/img', 'features.png')

@app.route('/assets/img/footer-bg.png')
def send_footer_bg_img():
    return send_from_directory('assets/img', 'footer-bg.png')

@app.route('/assets/img/hero-bg.png')
def send_hero_bg_img():
    return send_from_directory('assets/img', 'hero-bg.png')

@app.route('/assets/img/hero-img.png')
def send_hero_img():
    return send_from_directory('assets/img', 'hero-img.png')

@app.route('/assets/img/hero-img.svg')
def send_hero_svg():
    return send_from_directory('assets/img', 'hero-img.svg')

@app.route('/assets/img/logo-main.png')
def send_logo_main_img():
    return send_from_directory('assets/img', 'logo-main.png')

@app.route('/assets/img/logo.png')
def send_logo_img():
    return send_from_directory('assets/img', 'logo.png')

@app.route('/assets/img/pricing-business.png')
def send_pricing_business_img():
    return send_from_directory('assets/img', 'pricing-business.png')

@app.route('/assets/img/pricing-free.png')
def send_pricing_free_img():
    return send_from_directory('assets/img', 'pricing-free.png')

@app.route('/assets/img/pricing-starter.png')
def send_pricing_starter_img():
    return send_from_directory('assets/img', 'pricing-starter.png')

@app.route('/assets/img/pricing-ultimate.png')
def send_pricing_ultimate_img():
    return send_from_directory('assets/img', 'pricing-ultimate.png')

@app.route('/assets/img/S logo1.png')
def send_Slogo1_img():
    return send_from_directory('assets/img', 'S logo1.png')

@app.route('/assets/img/S logo2.png')
def send_Slogo2_img():
    return send_from_directory('assets/img', 'S logo2.png')

@app.route('/assets/img/S logo3.jpg')
def send_Slogo3_img():
    return send_from_directory('assets/img', 'S logo3.jpg')

@app.route('/assets/img/S logo4.png')
def send_Slogo4_img():
    return send_from_directory('assets/img', 'S logo4.png')

@app.route('/assets/img/S logo5.png')
def send_Slogo5_img():
    return send_from_directory('assets/img', 'S logo5.png')

@app.route('/assets/img/team-shape.svg')
def send_team_shape_svg():
    return send_from_directory('assets/img', 'team-shape.svg')

@app.route('/assets/img/values-1.png')
def send_value1_img():
    return send_from_directory('assets/img', 'values-1.png')

@app.route('/assets/img/values-2.png')
def send_value2_img():
    return send_from_directory('assets/img', 'values-2.png')

@app.route('/assets/img/values-3.png')
def send_value3_img():
    return send_from_directory('assets/img', 'values-3.png')
# img -end
# js
@app.route('/assets/js/ev.js')
def send_ev_js():
    return send_from_directory('assets/js', 'ev.js')

@app.route('/assets/js/main.js')
def send_main_js():
    return send_from_directory('assets/js', 'main.js')

@app.route('/assets/js/script1.js')
def send_script1_js():
    return send_from_directory('assets/js', 'script1.js')

@app.route('/assets/js/script2.js')
def send_script2_js():
    return send_from_directory('assets/js', 'script2.js')

@app.route('/assets/js/script3.js')
def send_script3_js():
    return send_from_directory('assets/js', 'script3.js')

@app.route('/assets/js/script4.js')
def send_script4_js():
    return send_from_directory('assets/js', 'script4.js')

@app.route('/assets/js/script5.js')
def send_script5_js():
    return send_from_directory('assets/js', 'script5.js')

@app.route('/assets/js/script6.js')
def send_script6_js():
    return send_from_directory('assets/js', 'script6.js')
# js -end
#vendor
#aos
@app.route('/assets/vendor/aos/aos.cjs.js')
def send_aos_cjs_js():
    return send_from_directory('assets/vendor/aos', 'aos.cjs.js')

@app.route('/assets/vendor/aos/aos.css')
def send_aos_css():
    return send_from_directory('assets/vendor/aos', 'aos.css')

@app.route('/assets/vendor/aos/aos.esm.js')
def send_aos_esm_js():
    return send_from_directory('assets/vendor/aos', 'aos.esm.js')

@app.route('/assets/vendor/aos/aos.js')
def send_aos_js():
    return send_from_directory('assets/vendor/aos', 'aos.js')

@app.route('/assets/vendor/aos/aos.js.map')
def send_aos_js_map():
    return send_from_directory('assets/vendor/aos', 'aos.js.map')
# aos -end
# bootstrap
# css
@app.route('/assets/vendor/bootstrap/css/bootstrap-grid.css')
def send_bootstrap_grid_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-grid.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap-grid.css.map')
def send_bootstrap_grid_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-grid.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap-grid.min.css')
def send_bootstrap_grid_min_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-grid.min.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap-grid.min.css.map')
def send_bootstrap_grid_min_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-grid.min.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap-grid.rtl.css')
def send_bootstrap_grid_rtl_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-grid.rtl.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap-grid.rtl.css.map')
def send_bootstrap_grid_rtl_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-grid.rtl.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap-grid.rtl.min.css')
def send_bootstrap_grid_rtl_min_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-grid.rtl.min.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap-grid.rtl.min.css.map')
def send_bootstrap_grid_rtl_min_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-grid.rtl.min.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap-reboot.css')
def send_bootstrap_reboot_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-reboot.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap-reboot.css.map')
def send_bootstrap_reboot_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-reboot.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap-reboot.min.css')
def send_bootstrap_reboot_min_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-reboot.min.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap-reboot.min.css.map')
def send_bootstrap_reboot_min_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-reboot.min.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap-rtl.css')
def send_bootstrap_rtl_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-rtl.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap-rtl.css.map')
def send_bootstrap_rtl_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-rtl.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap-rtl.min.css')
def send_bootstrap_rtl_min_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-rtl.min.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap-rtl.min.css.map')
def send_bootstrap_rtl_min_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-rtl.min.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap-utilities.css')
def send_bootstrap_utilities_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-utilities.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap-utilities.css.map')
def send_bootstrap_utilities_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-utilities.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap-utilities.min.css')
def send_bootstrap_utilities_min_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-utilities.min.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap-utilities.min.css.map')
def send_bootstrap_utilities_min_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-utilities.min.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap-utilities.rtl.css')
def send_bootstrap_utilities_rtl_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-utilities.rtl.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap-utilities.rtl.css.map')
def send_bootstrap_utilities_rtl_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-utilities.rtl.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap-utilities.rtl.min.css')
def send_bootstrap_utilities_rtl_min_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-utilities.rtl.min.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap-utilities.rtl.min.css.map')
def send_bootstrap_utilities_rtl_min_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap-utilities.rtl.min.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap.css')
def send_bootstrap_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap.css.map')
def send_bootstrap_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap.min.css')
def send_bootstrap_min_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap.min.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap.min.css.map')
def send_bootstrap_min_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap.min.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap.rtl.css')
def send_bootstrap_rtl1_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap.rtl.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap.rtl.css.map')
def send_bootstrap_rtl1_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap.rtl.css.map')

@app.route('/assets/vendor/bootstrap/css/bootstrap.rtl.min.css')
def send_bootstrap_rtl1_min_css():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap.rtl.min.css')

@app.route('/assets/vendor/bootstrap/css/bootstrap.rtl.min.css.map')
def send_bootstrap_rtl1_min_css_map():
    return send_from_directory('assets/vendor/bootstrap/css', 'bootstrap.rtl.min.css.map')
# css -end
# js
@app.route('/assets/vendor/bootstrap/js/bootstrap.bundle.js')
def send_bootstrap_bundle_js():
    return send_from_directory('assets/vendor/bootstrap/js', 'bootstrap.bundle.js')

@app.route('/assets/vendor/bootstrap/js/bootstrap.bundle.js.map')
def send_bootstrap_bundle_js_map():
    return send_from_directory('assets/vendor/bootstrap/js', 'bootstrap.bundle.js.map')

@app.route('/assets/vendor/bootstrap/js/bootstrap.bundle.min.js')
def send_bootstrap_bundle_min_js():
    return send_from_directory('assets/vendor/bootstrap/js', 'bootstrap.bundle.min.js')

@app.route('/assets/vendor/bootstrap/js/bootstrap.bundle.min.js.map')
def send_bootstrap_bundle_min_js_map():
    return send_from_directory('assets/vendor/bootstrap/js', 'bootstrap.bundle.min.js.map')

@app.route('/assets/vendor/bootstrap/js/bootstrap.esm.js')
def send_bootstrap_esm_js():
    return send_from_directory('assets/vendor/bootstrap/js', 'bootstrap.esm.js')

@app.route('/assets/vendor/bootstrap/js/bootstrap.esm.js.map')
def send_bootstrap_esm_js_map():
    return send_from_directory('assets/vendor/bootstrap/js', 'bootstrap.esm.js.map')

@app.route('/assets/vendor/bootstrap/js/bootstrap.esm.min.js')
def send_bootstrap_esm_min_js():
    return send_from_directory('assets/vendor/bootstrap/js', 'bootstrap.esm.min.js')

@app.route('/assets/vendor/bootstrap/js/bootstrap.esm.min.js.map')
def send_bootstrap_esm_min_js_map():
    return send_from_directory('assets/vendor/bootstrap/js', 'bootstrap.esm.min.js.map')

@app.route('/assets/vendor/bootstrap/js/bootstrap.js')
def send_bootstrap_js():
    return send_from_directory('assets/vendor/bootstrap/js', 'bootstrap.js')

@app.route('/assets/vendor/bootstrap/js/bootstrap.js.map')
def send_bootstrap_js_map():
    return send_from_directory('assets/vendor/bootstrap/js', 'bootstrap.js.map')

@app.route('/assets/vendor/bootstrap/js/bootstrap.min.js')
def send_bootstrap_min_js():
    return send_from_directory('assets/vendor/bootstrap/js', 'bootstrap.min.js')

@app.route('/assets/vendor/bootstrap/js/bootstrap.min.js.map')
def send_bootstrap_min_js_map():
    return send_from_directory('assets/vendor/bootstrap/js', 'bootstrap.min.js.map')
# js -end
# bootstrap -end
# bootstrap-icons
# fonts
@app.route('/assets/vendor/bootstrap-icons/fonts/bootstrap-icons.woff')
def send_bootstrap_icons_woff():
    return send_from_directory('assets/vendor/bootstrap-icons/fonts', 'bootstrap-icons.woff')

@app.route('/assets/vendor/bootstrap-icons/fonts/bootstrap-icons.woff2')
def send_bootstrap_icons_woff2():
    return send_from_directory('assets/vendor/bootstrap-icons/fonts', 'bootstrap-icons.woff2')
# fonts -end
@app.route('/assets/vendor/bootstrap-icons/bootstrap-icons.css')
def send_bootstrap_icons_css():
    return send_from_directory('assets/vendor/bootstrap-icons', 'bootstrap-icons.css')

@app.route('/assets/vendor/bootstrap-icons/bootstrap-icons.json')
def send_bootstrap_iconsj_json():
    return send_from_directory('assets/vendor/bootstrap-icons', 'bootstrap-icons.json')

@app.route('/assets/vendor/bootstrap-icons/bootstrap-icons.min.css')
def send_bootstrap_icons_min_css():
    return send_from_directory('assets/vendor/bootstrap-icons', 'bootstrap-icons.min.css')

@app.route('/assets/vendor/bootstrap-icons/bootstrap-icons.scss')
def send_bootstrap_iconss_scss():
    return send_from_directory('assets/vendor/bootstrap-icons', 'bootstrap-icons.scss')
# bootstrap-icons -end
# glightbox
# css 
@app.route('/assets/vendor/glightbox/css/glightbox.css')
def send_glightbox_css():
    return send_from_directory('assets/vendor/glightbox/css', 'glightbox.css')

@app.route('/assets/vendor/glightbox/css/glightbox.min.css')
def send_glightbox_min_css():
    return send_from_directory('assets/vendor/glightbox/css', 'glightbox.min.css')

@app.route('/assets/vendor/glightbox/css/plyr.css')
def send_plyr_css():
    return send_from_directory('assets/vendor/glightbox/css', 'plyr.css')

@app.route('/assets/vendor/glightbox/css/plyr.min.css')
def send_plyr_min_css():
    return send_from_directory('assets/vendor/glightbox/css', 'plyr.min.css')
# css -end
# js
@app.route('/assets/vendor/glightbox/js/glightbox.js')
def send_glightbox_js():
    return send_from_directory('assets/vendor/glightbox/js', 'glightbox.js')

@app.route('/assets/vendor/glightbox/js/glightbox.min.js')
def send_glightbox_min_js():
    return send_from_directory('assets/vendor/glightbox/js', 'glightbox.min.js')
# js -end
# glightbox -end
# isotope-layout
@app.route('/assets/vendor/isotope-layout/isotope.pkgd.js')
def send_isotope_pkgd_js():
    return send_from_directory('assets/vendor/isotope-layout', 'isotope.pkgd.js')

@app.route('/assets/vendor/isotope-layout/isotope.pkgd.min.js')
def send_isotope_pkgd_min_js():
    return send_from_directory('assets/vendor/isotope-layout', 'isotope.pkgd.min.js')
# isotope-layout -end
# php-email-form
@app.route('/assets/vendor/php-email-form/validate.js')
def send_validate_js():
    return send_from_directory('assets/vendor/php-email-form', 'validate.js')
# php-email-form -end
# purecounter
@app.route('/assets/vendor/purecounter/purecounter_vanilla.js')
def send_purecounte_vanilla_js():
    return send_from_directory('assets/vendor/purecounter', 'purecounter_vanilla.js')

@app.route('/assets/vendor/purecounter/purecounter_vanilla.js.map')
def send_purecounte_vanilla_js_map():
    return send_from_directory('assets/vendor/purecounter', 'purecounter_vanilla.js.map')
# purecounter -end
# remixicon
@app.route('/assets/vendor/remixicon/remixicon.css')
def send_remixicon_css():
    return send_from_directory('assets/vendor/remixicon', 'remixicon.css')

@app.route('/assets/vendor/remixicon/remixicon.eot')
def send_remixicon_eot():
    return send_from_directory('assets/vendor/remixicon', 'remixicon.eot')

@app.route('/assets/vendor/remixicon/remixicon.glyph.json')
def send_remixicon_glyph_json():
    return send_from_directory('assets/vendor/remixicon', 'remixicon.glyph.json')

@app.route('/assets/vendor/remixicon/remixicon.less')
def send_remixicon_less():
    return send_from_directory('assets/vendor/remixicon', 'remixicon.less')

@app.route('/assets/vendor/remixicon/remixicon.svg')
def send_remixicon_svg():
    return send_from_directory('assets/vendor/remixicon', 'remixicon.svg')

@app.route('/assets/vendor/remixicon/remixicon.symbol.svg')
def send_remixicon_symbol_svg():
    return send_from_directory('assets/vendor/remixicon', 'remixicon.symbol.svg')

@app.route('/assets/vendor/remixicon/remixicon.ttf')
def send_remixicon_ttf():
    return send_from_directory('assets/vendor/remixicon', 'remixicon.ttf')

@app.route('/assets/vendor/remixicon/remixicon.woff')
def send_remixicon_woff():
    return send_from_directory('assets/vendor/remixicon', 'remixicon.woff')

@app.route('/assets/vendor/remixicon/remixicon.woff2')
def send_remixicon_woff2():
    return send_from_directory('assets/vendor/remixicon', 'remixicon.woff2')
# remixicon -end
# swiper
@app.route('/assets/vendor/swiper/swiper-bundle.min.css')
def send_swiper_bundle_min_css():
    return send_from_directory('assets/vendor/swiper', 'swiper-bundle.min.css')

@app.route('/assets/vendor/swiper/swiper-bundle.min.js')
def send_swiper_bundle_min_js():
    return send_from_directory('assets/vendor/swiper', 'swiper-bundle.min.js')

@app.route('/assets/vendor/swiper/swiper-bundle.min.js.map')
def send_swiper_bundle_min_js_map():
    return send_from_directory('assets/vendor/swiper', 'swiper-bundle.min.js.map')
# swiper -end
#vendor -end
# assets -end

# Information
@app.route('/Information/PPhishing.mp4')
def send_PPhishing_video():
    return send_from_directory('Information', 'PPhishing.mp4')

@app.route('/Information/Scam.mp4')
def send_Scam_video():
    return send_from_directory('Information', 'Scam.mp4')

@app.route('/Information/Tactics.mp4')
def send_Tactics_video():
    return send_from_directory('Information', 'Tactics.mp4')

@app.route('/Information/Types of Phishing.mp4')
def send_TypesofPhishing_video():
    return send_from_directory('Information', 'Types of Phishing.mp4')

@app.route('/Information/Unmasking Phishing.mp4')
def send_UnmaskingPhishing_video():
    return send_from_directory('Information', 'Unmasking Phishing.mp4')

@app.route('/Information/What is Phishing.mp4')
def send_WhatisPhishing_video():
    return send_from_directory('Information', 'What is Phishing.mp4')
# Information -end

if __name__ == "__main__":
    # unittest.main()
    app.run(debug=True)