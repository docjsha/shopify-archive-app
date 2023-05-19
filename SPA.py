import pandas as pd
import streamlit as st


def main():
    st.set_page_config(
        page_title = 'SPA',
        page_icon = '🗄️',
    )
    
    st.title('Shopify Product Archive')
    
    file = st.file_uploader(f'Upload a json file', type=['json'])
    if file:
        try:
            df = pd.read_json(file)
            if 'products' in df.columns:
                df = df['products'].apply(pd.Series)
                st.header('Raw data:')
                st.dataframe(df)
                st.header('Products:')
                with st.spinner('Loading images...'):
                    for i in range(len(df)):
                        st.subheader(df.iloc[i].title)
                        try:
                            price = df.iloc[i]['variants'][0]['price']
                        except:
                            price = None
                        if price is not None:
                            st.write(f'Price: ${price}')
                        st.write(df.iloc[i]['body_html'], unsafe_allow_html=True)
                        for img in df.iloc[i].images:
                            st.image(img['src'], use_column_width=True)
                        st.markdown('---')
        except:
            st.warning('Please check the uploaded json file is valid.')


    # Hide footer
    hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}
    """
    # Hide hamburger menu
    st.markdown(hide_footer_style, unsafe_allow_html=True)
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)



if __name__ == "__main__":
    main()