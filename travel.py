import streamlit as st
import io
from PIL import Image

st.title("Tasmania - Dec 8 - Dec 19 2022")

st.header("Friday Dec 9")

col1, col2, col3 = st.columns([4,1,1])

with col1:
    st.header("Day 1")
    image = Image.open('./assets/img/Day9.png')
    st.image(image, caption="Day 1")

with col2:
    st.header("Travel Plan")
    st.write("Hobart to Campbell Town")
    st.write("Campbell Town to Launceston")
    st.write("Launceston to Cataract Gorge")

with col3:
    st.header("Food Stop")
    st.write("Bakery 31 - Scallop Pie")


st.header("Saturday Dec 10")

col1, col2, col3 = st.columns([4,1,1])

with col1:
    st.header("Day 2")
    image = Image.open('./assets/img/Day10.png')
    st.image(image, caption="Day 2")

with col2:
    st.header("Travel Plan")
    st.write("Launceston to Bridestowe Lavender Farm")
    st.write("Bridestowe to Little Blue Lake")
    st.write("Little Blue Lake to Anson Bay")
    st.write("Anson Bay to Bay of Fires")
    st.write("Bay of Fires to Binalong Bay")
    st.write("Binalong Bay to St Helens")
    st.write("St Helens to Jacobs Ladder")
    st.write("Jacobs Ladder to Launceston")

with col3:
    st.header("Food Stop")


# Cradle Mountain

st.header("Sunday Dec 11")

col1, col2, col3 = st.columns([4,1,1])

with col1:
    st.header("Day 3")
    image = Image.open('./assets/img/Day11.png')
    st.image(image, caption="Day 3")

with col2:
    st.header("Travel Plan")
    st.write("Launceston to Cradle Mountain")
    st.write("Cradle Mountain to Dove Lake")
    st.write("Dove Lake to Mole Creek Caves")
    st.write("Mole Creek Caves to Alum Cliffs")
    st.write("Alum Cliffs to Stephen Tasmania Honey")
    st.write("Stephen Tasmania Hoeny to Liffey Falls")
    st.write("Liffey Falls to Launceston")

with col3:
    st.header("Food Stop")

# Shopping in Launceston

st.header("Monday Dec 12")

col1, col2, col3 = st.columns([4,1,1])

with col1:
    st.header("Day 4")
    image = Image.open('./assets/img/Day12.png')
    st.image(image, caption="Day 4")

with col2:
    st.header("Travel Plan")
    st.write("Launceston to The Nut")
    st.write("The Nut to Table Cape Tulip Farm")
    st.write("Table Cape Tulip Farm to Burnie")
    st.write("Burnie to Turners Beach")
    st.write("Turners Beach to House of Anvers")
    st.write("House of Anvers to Ashgroove Cheese")
    st.write("Ashgroove Cheese to Christmas Hills Raspberry Cafe")

with col3:
    st.header("Food Stop")

# Bicheno

st.header("Tuesday Dec 13")

col1, col2, col3 = st.columns([4,1,1])

with col1:
    st.header("Day 5")
    image = Image.open('./assets/img/Day13.png')
    st.image(image, caption="Day 5")

with col2:
    st.header("Travel Plan")
    st.write("Launceston to Bicheno")
    st.write("Bicheno to WineGlass Bay")
    st.write("WineGlass Bay to Eagle Hawk")
    st.write("Eagle Hawk to Freycinet")
    st.write("Freycinet to Hobart")

with col3:
    st.header("Food Stop")

# Day Hoabrt
st.header("Wednesday Dec 14")

col1, col2, col3 = st.columns([4,1,1])

with col1:
    st.header("Day 6")
    image = Image.open('./assets/img/Day14.png')
    st.image(image, caption="Day 6")

with col2:
    st.header("Travel Plan")
    st.write("Hobart to Mt Field National Park")
    st.write("Mt Field To Russell Falls")
    st.write("Russell Falls to Treetop Walks")
    st.write("Treetop Walks to Mt Wellington")
    st.write("Mt Wellington to Franklin Wharf")
    st.write("Franklin Wharf to Hobart")

with col3:
    st.header("Food Stop")
  
st.header("Thursday Dec 15")

col1, col2, col3 = st.columns([3,1,1])

with col1:
    st.header("Day 7")
    image = Image.open('./assets/img/Day15.png')
    st.image(image, caption="Day 7")

with col2:
    st.header("Travel Plan")
    st.write("Hobart to Bruny Island")
    st.write("Go back to Ferry Point by 5 pm - Last Ferry 6.30 pm")
    st.write("Bruny Island to Hobart")

with col3:
    st.header("Food Stop")
    st.write("Get Shucked - Breakfast")
    st.write("Hotel Bruny - Lunch")
    st.write("Cape Bruny Oysters - Lunch")

# Day
st.header("Friday Dec 16")

col1, col2, col3 = st.columns([3,1,1])

with col1:
    st.header("Day 8")
    image = Image.open('./assets/img/Day16.png')
    st.image(image,caption="Day 8")

with col2:
    st.header("Travel Plan")
    st.write("Hobart to Tahune Adventure")
    st.write("Tahune Adventure to Sphink Lookout")
    st.write("Sphink Looktout to Sorell Fruit Farm")
    st.write("Sorell Fruit Farm to Seven Mile Beach")
    st.write("Seven Mile Beach to Taroona")

with col3:
    st.header("Food Stop")
   
# Day
st.header("Saturday Dec 17")

col1, col2, col3 = st.columns([3,1,1])

with col1:
    st.header("Day 9")
    image = Image.open('./assets/img/Day17.png')
    st.image(image, caption="Day 9")

with col2:
    st.header("Travel Plan")
    st.write("Salamanca Place")
    st.write("The Farm Gate Market operates every Sunday along Bathurst Street in the CBD between 8.30am and 1pm")
    st.write("MONA Museum")
    st.write("Brooke Street Pier")
    st.write("Battery Point - Village")
    st.write("Huon Valley")

with col3:
    st.header("Food Stop")
    st.write("Finally, no visit to Battery Point is complete with a visit to the fabulous Jackman and McRoss.")
    st.write("If you’re looking for some sustenance in between browsing, head to nearby Bathurst St where you’ll find Raspberry Fool (cafe/bakery), Bury Me Standing (bagels, coffee and treats) and the Criterion St Cafe (all day cafe and coffee). This is the area where the Farm Gate market is held on Sundays.")
    st.write("We opted for more casual tapas style dinners at Aloft, The Glasshouse  at Brooke St Pier and Smolt in Salamanca Square")


# Day
st.header("Sunday Dec 18")

col1, col2, col3 = st.columns([3,1,1])

with col1:
    st.header("Day 10")
    image = Image.open('./assets/img/Day18.png')
    st.image(image, caption="Day 10")

with col2:
    st.header("Travel Plan")
    st.write("Hobart to Mount Brown")
    st.write("Mount Brown to Maingon Blowhole")
    st.write("Maingon Blowhole to Remarkable Cave")
    st.write('Remarlable Cave to Port Arthur Historic Site')
    st.write("Port Arthur to WaterBay Lookout")
    st.write("Waterbay to Paterson Arc")    
    st.write("Paterson Arc to Devils Kitchen")
    st.write("Devils Kitchen to Tasman Arc")    
    st.write("Tasman Arc to Fossil Bay Blowhole")
    st.write("Fossil Bay Blowhole to Eagle Hawk Neck")
    st.write("Eagle Hawk Neck to Tessellated Pavement")
    st.write("Tesellataed Pavement to Pirates Bay lookout")
    st.write("Pirates Bay Lookout to Hobart")
 
 

with col3:
    st.header("Food Stop")

# Day

st.header("Monday Dec 19")

col1, col2, col3 = st.columns([3,1,1])

with col1:
    st.header("Day 11")
    image = Image.open('./assets/img/Day15.png')
    st.image(image, caption="Day 11")

with col2:
    st.header("Travel Plan")
    st.write("Hobart to Airport")

with col3:
    st.header("Food Stop")
    

# Timeline
