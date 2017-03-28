from collections import namedtuple

from flask import Flask, render_template

app = Flask(__name__)


Offer = namedtuple('Offer', ['long_name', 'short_name', 'text_id', 'price', 'image_url'])

OFFERS = [
  Offer(long_name="L'Etoile Anti Wrinkle Complex",
       short_name="L'Etoile",
       text_id='letoile',
       price=4.95,
       image_url='http://imgur.com/Kmuh0n0.png'
       ),
  Offer(long_name="Allegro Antiaging Cream",
       short_name="Allegro",
       text_id='allegro',
       price=4.95,
       image_url='http://i.imgur.com/jOw0QFp.png'
       ),
  Offer(long_name='Renewing Serum CE',
       short_name='Renewing Serum CE',
       text_id='renewing',
       price=4.95,
       image_url='https://d3oimv5qppjae2.cloudfront.net/findbeautyandtruth.com/rs03/product.png'
       ),
  Offer(long_name='Erase/Repair HA',
       short_name='Erase/Repair',
       text_id='erase',
       price=4.95,
       image_url='http://d3oimv5qppjae2.cloudfront.net/findbeautyandtruth.com/er06/product.png'
       ),
  Offer(long_name='Borealis Anti-Aging Face Cream',
       short_name='Borealis',
       text_id='borealis',
       price=4.95,
       image_url='http://imgur.com/F0fdSpD.png'
       ),
  Offer(long_name='Alucia Ultra Premium Anti-Wrinkle Complex',
       short_name='Alucia',
       text_id='alucia',
       price=4.95,
       image_url='http://imgur.com/n8l5Zos.png'
       ),
  Offer(long_name='Aviqua Ultra Premium Anti-Wrinkle Skin Cream',
       short_name='Aviqua',
       text_id='aviqua',
       price=4.95,
       image_url='http://imgur.com/xg8SPks.png',
       ),
  Offer(long_name='DermaFi Snake Venom Peptide Cream',
        short_name='DermaFi',
        text_id='dermafi',
        price=4.95,
        image_url='http://imgur.com/PJ1L9pm.png'
        ),
  Offer(long_name='Hydroluxe Wrinkle',
        short_name='Hydroluxe',
        text_id='hydroluxe',
        price=4.95,
        image_url='http://skincare.shapenews.online/OfferImages/Hydroluxe.jpg'
        ),
  Offer(long_name='Parisian Glow Revitalizing Moisturizer',
        short_name='Parisian Glow',
        text_id='parisian',
        price=4.95,
        image_url='http://imgur.com/m3LkRmp.png'
        ),
  Offer(long_name='Premium Brand Anti Aging Formula',
        short_name='Premium Brand',
        text_id='premium',
        price=4.95,
        image_url='http://skincare.shapenews.online/OfferImages/Premium.jpg'
        ),
  Offer(long_name='True Skin Anti Aging',
        short_name='True Skin',
        text_id='trueskin',
        price=4.95,
        image_url='http://skincare.shapenews.online/OfferImages/TrueSkin.png'
        ),
  Offer(long_name='Essence of Argan',
        short_name='Essence',
        text_id='essence',
        price=4.95,
        image_url='http://skincare.shapenews.online/OfferImages/essen.png'
        ),
  Offer(long_name="Z'Amour Luxury Anti-Aging Beauty Matrix",
        short_name="Z'Amour",
        text_id='zamour',
        price=4.95,
        image_url='http://skincare.shapenews.online/OfferImages/zamour-matrix.png'
        ),
]


@app.route('/abc/offer/<int:offer_pos>/')
def abc_index(offer_pos):
  offerobj = OFFERS[offer_pos]
  return render_template('abc_index.html',
                        offer=offerobj
                        )
