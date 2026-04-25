import streamlit as st
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

model = load_model('cotton_disease_model.h5')


class_info = {
    'Aphids': {
        'treatment': 'To control aphids,'
        ' you can use insecticidal soaps such as Safer Brand Insect Killing Soap or a neem oil solution like that from Garden Safe. For a biological control approach, introduce beneficial insects like ladybugs and lacewings, which are natural predators of aphids.',
        'image': 'https://www.khethari.com/cdn/shop/articles/apdids_in_cotton2.webp?v=1720672823'  # TODO: Replace with your own image URL
    },
    'Army worm': {
        'treatment': 'For armyworm infestations, apply a product containing Bacillus thuringiensis (Bt), such as Monterey B.t. Biological Insecticide. Alternatively, you can use a pyrethrin-based insecticide like Bonide Pyrethrin Garden Insect Spray. For smaller infestations, handpicking the worms off the plants is also effective.',
        'image': 'https://media.sciencephoto.com/image/z3551301/800wm'  # TODO: Replace with your own image URL
    },
    'Bacterial Blight': {
        'treatment': 'Bacterial blight is best managed through preventative measures. Use certified disease-free seeds and practice crop rotation. If the disease is present, a copper-based bactericide such as Bonide Copper Fungicide can help slow its spread.',
        'image': 'https://www.plantdiseases.org/sites/default/files/styles/plant_disease_content_type_325x325_/public/plant_disease/images/0337.jpg?itok=swtXStdm'  # TODO: Replace with your own image URL
    },
    'Healthy': {
        'treatment': 'Your plant appears to be in excellent health. Continue to provide it with proper watering, adequate sunlight, and a balanced fertilizer to maintain its vigor.',
        'image': 'https://www.researchgate.net/publication/369357236/figure/fig25/AS:11431281261019582@1721354874807/A-healthy-cotton-plant-leaf-having-no-spots.png'  # TODO: Replace with your own image URL
    },
    'Powdery Mildew': {
        'treatment': 'To treat powdery mildew, apply a fungicide containing sulfur, such as Bonide Sulfur Plant Fungicide, or one with potassium bicarbonate, like Monterey Bi-Carb Fungicide. A homemade remedy of one part milk to ten parts water can also be effective when sprayed on the leaves.',
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe3pZKGEKEYec2BbxRxD9l9jec-WvXfzOr4A&s'  # TODO: Replace with your own image URL
    },
    'Target Spot': {
        'treatment': 'Control target spot by applying a fungicide containing chlorothalonil, such as Bonide Fung-onil Fungicide, or one with myclobutanil, like Spectracide Immunox Multi-Purpose Fungicide. It is also important to remove and destroy infected leaves to prevent the disease from spreading.',
        'image': 'https://guide.utcrops.com/wp-content/uploads/2017/04/Target-Spot-Typical-Lesion.jpg'  # TODO: Replace with your own image URL
    }
}

# Sidebar background image (hosted version of your Shutterstock image)
COTTON_IMAGE_URL = "https://www.shutterstock.com/image-illustration/cotton-plant-stem-leaves-watercolor-600nw-2216118511.jpg"  # Replace with your own if needed
st.markdown(
    """
    <style>
    /* Full page background color */
    .stApp {
        background-color: #f5f5dc; /* Light brown or any hex code */
    }
    
     .block-container {
        background-color: #f5f5dc;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Custom CSS for styling
st.markdown(
    f"""
    <style>
  
    [data-testid="stSidebar"] > div:first-child {{
        background: linear-gradient(rgba(159, 214, 177, 0.7), rgba(159, 214, 177, 0.7)),
                    url("{COTTON_IMAGE_URL}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }}
    .stButton > button {{
        color: white;
        background-color: #2E8B57;
        border-radius: 12px;
        font-size: 18px;
        transition: 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    .stButton > button:hover {{
        background-color: #45a049;
        transform: scale(1.05);
    }}
    class_info {{
        font-family: "Segoe UI", sans-serif;
        color: #333;
        font-size: 16px;
        line-height: 1.6;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        background-color: #e8f5e9;
    }}
    # .treatment-card {{
    #     background-color: #ffffffee;
    #     padding: 1rem;
    #     border-radius: 10px;
    #     box-shadow: 0 3px 10px rgba(0,0,0,0.15);
    #     margin-top: 1rem;
    #     background-image: ("D:\OneDrive\Documents\CAI.course\deeplearning\ccoton\gardenimg.jpg");
    #     background-size: cover;
    #     background-repeat: no-repeat;
    #     background-position: center;
    #     color: #333;
    #     font-family: "Segoe UI", sans-serif;
    # }}
    </style>
    """,
    unsafe_allow_html=True
)
logo_url = "data:image/jpeg;base64,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"
logo_url1="https://png.pngtree.com/png-clipart/20231110/original/pngtree-cotton-plant-green-photo-png-image_13528205.png"
st.markdown(
    f"""
    <div style="display: flex; align-items: center; gap: 12px;">
        <img src="{logo_url1}" alt="logo" width="48" height="48">
        <h1 style="margin: 0; font-family:'Brush Script MT'; color: green; font-size:63px">Cotton Disease Classifier</h1>
    </div>
    """,
    unsafe_allow_html=True
)


with st.expander("📘 How to Use This App"):
    st.markdown("""
        <div style='font-family: "Segoe UI", sans-serif; font-size: 16px; line-height: 1.6; color: #333; padding: 20px; border-radius: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); background-color: #e8f5e9;'>
        <h4 style='font-size:23px; font-family:"Arial Black"; '>Follow these steps to get started:</h4>
        <ol>
            <li>Choose <b>Upload an image</b> or <b>Use webcam</b> from the sidebar.</li>
            <li>Upload or capture a clear image of a cotton leaf or stem.</li>
            <li>Click <b>🔍 Predict</b> to detect the disease.</li>
            <li>You'll see a prediction, confidence score, and treatment advice.</li>
        </ol>

        <hr style="margin-top: 10px; margin-bottom: 10px;">

        <b style='font-size: 20px; font-family: "Lucida Handwriting";'>🦠 Currently Supported Cotton Plant Conditions: (پہچانی جانے والی بیماریاں )</b>

        <ul style="list-style-type: none; padding-left: 0;">
            <li style="padding: 4px 0;">🌿 <b>Aphids – افڈز</b></li>
            <li style="padding: 4px 0;">🐛 <b>Army Worm – آرمی کیڑا</b></li>
            <li style="padding: 4px 0;">🦠 <b>Bacterial Blight – بیکٹیریل جھلساؤ</b></li>
            <li style="padding: 4px 0;">🌼 <b>Healthy – صحت مند</b></li>
            <li style="padding: 4px 0;">🍃 <b>Powdery Mildew سفوفی پھپھوند</b></li>
            <li style="padding: 4px 0;">🎯 <b>Target Spot – نشانی دھبہ<b></li>
        </ul>

        </div>
    """, unsafe_allow_html=True)


# Sidebar option
# st.sidebar.image( "D:\OneDrive\Documents\CAI.course\deeplearning\ccoton\gardenimg.jpg", use_container_width=True)

option = st.sidebar.radio("📸 Choose an option:", ("Upload an image", "Use webcam"))
# Upload image option

# Prediction function
def predict(image_path):
    # img = image.load_img(image_path, target_size=(224, 224))
    img = Image.open(image_path).convert('RGB')
    img = img.resize((224, 224))
    # img_array = image.img_to_array(img)

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction[0])
    predicted_class_name = list(class_info.keys())[predicted_class_index]
    confidence = np.max(prediction[0])
    return predicted_class_name, confidence

# Image Upload Workflow
if option == "Upload an image":
    uploaded_file = st.file_uploader("📤 Upload an image (jpg/jpeg/jfif)", type=["jpg", "jpeg", "jfif"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption='🖼️ Uploaded Image', use_container_width=True)

        if st.button('🔍 Predict'):
            with open("temp_image.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())
            class_name, conf = predict("temp_image.jpg")

            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"<h4 style='color:red;'>✅ Prediction: <b>{class_name}</b></h4>", unsafe_allow_html=True)
                st.progress(int(conf * 100))
                st.markdown("<div class='treatment-card'>", unsafe_allow_html=True)
                # st.subheader("🩺 Treatment Advice")
                st.markdown("<h4 style='color:#2E8B57;'>🩺 Treatment Advice</h4>", unsafe_allow_html=True)
                st.write(class_info[class_name]['treatment'])
                st.markdown("</div>", unsafe_allow_html=True)
            with col2:
                st.image(class_info[class_name]['image'], caption=f"{class_name}", use_container_width=True)

# Webcam Capture Workflow
elif option == "Use webcam":
    img_file_buffer = st.camera_input("📷 Take a picture")
    if img_file_buffer is not None:
        img = Image.open(img_file_buffer)
        st.image(img, caption='🖼️ Captured Image', use_container_width=True)

        if st.button('🔍 Predict'):
            with open("temp_image.jpg", "wb") as f:
                f.write(img_file_buffer.getbuffer())
            class_name, conf = predict("temp_image.jpg")

            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"<h4 style='color:#2E8B57;'>✅ Prediction: <b>{class_name}</b></h4>", unsafe_allow_html=True)
                st.progress(int(conf * 100))
                st.subheader("🩺 Treatment Advice")
                st.write(class_info[class_name]['treatment'])
                st.markdown("</div>", unsafe_allow_html=True)
                
            with col2:
                st.image(class_info[class_name]['image'], caption=f"{class_name}", use_column_width=True)
