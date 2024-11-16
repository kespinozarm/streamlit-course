# 1. Text inputs

favorite_color = st.text_input("What's your favorite color:")
st.write(f"My favorite color is {favorite_color}")

favorite_animal= st.text_input("What's your favorite animal:")
st.write(f"My favorite animal is {favorite_animal}")

lucky_number= st.number_input("What's your lucky number:", step = 1)
st.write(f"My lucky number is {lucky_number}")

superpower = st.selectbox("Choose your superpower:", ["Flying", "Invisibiblity", "Fast as flash"])



if st.button("Generate my superhero name 🦹🏻") == True:
    st.header(f"Your superhero name is: {favorite_animal} of {favorite_color} {lucky_number}")
    st.header(f"And your superpower is: {superpower}")
