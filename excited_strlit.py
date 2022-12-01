import streamlit as st 
import spot1
import from_here
def main():
    st.title("Ello there matey, listen to our top suggested while you keep up the excitement. ;)")
    menu = ["Shut Up And Dance", "Dheere Dheere Se Meri Zindagi Mein Aana", "Hymn for the Weekend"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Shut Up And Dance":
        
        st.subheader("Listen To Shut Up And Dance")
        images = ['shutup.png']
        st.image(images, use_column_width=True, caption=["Music mania"] * len(images))
        if st.button("listen"):
            spot1.get_song(choice)
        if st.button("like"):
            st.subheader("Keep dancing to our beats, choose from them below")
            lst = list(set(from_here.final(choice)))
        
            for i in lst:
                if st.button(i):
                    spot1.get_song(i)

                

            
                
           
                
                    
                    # spot1.get_song(i)
             #spot1.get_song(choice)
        # elif st.button("see next"):
        #     return
    elif choice == "Dheere Dheere Se Meri Zindagi Mein Aana":
        st.subheader("Listen To Dheere Dheere Se Meri Zindagi Mein Aana")
        images = ['dheere.JPG']
        st.image(images, use_column_width=True, caption=["some generic text"] * len(images))
        if st.button("listen"):
            spot1.get_song(choice)
        if st.button("like"):
            st.subheader("oooo, did she say yes? keep the enthusiasm up by listening to:")
            lst = list(set(from_here.final(choice)))
            
            for i in lst:
                if st.button(i):
                    spot1.get_song(i)
            #return #spot1.get_song(choice)
        # elif st.button("see next"):
        #     return

    elif choice == "Hymn for the Weekend":
        st.subheader("Listen To Hymn for the Weekend")
        images = ['hymn.JPG']
        st.image(images, use_column_width=True, caption=["music mania"] * len(images))
        if st.button("listen"):
            spot1.get_song(choice)
        if st.button("like"):
            st.subheader("Perfect collection for your perfect weekend")
            lst = list(set(from_here.final(choice)))
            
            for i in lst:
                if st.button(i):
                    spot1.get_song(i)
        # elif st.button("see next"):
        #     return

    # elif choice == "Dukh Ke Din Men Koi Nahine":
    #     st.subheader("Listen To Dukh Ke Din Men Koi Nahine")
    #     if st.button("listen"):
    #         spot1.get_song(choice)
    #     if st.button("like"):
    #         lst = list(set(from_here.final(choice)))
            
    #         for i in lst:
    #             if st.button(i):
    #                 spot1.get_song(i)
        
         

    

             


            

    # populate playlist with recommended tracks
            
           

        

        #create()
    # elif choice == "The happy song":
    #     st.subheader("The happy song")
    #     #spot1.get_song(choice)
    #     #read()
    # elif choice == "comethru":
    #     st.subheader("hi")
    #     #spot1.get_song(choice)
    #     #update()
    # elif choice == "someone to you":
    #     st.subheader("Happy 4")
    #    # spot1.get_song(choice)
    #     #delete()
    # # else:
    #     st.subheader("About tasks")
if __name__ == '__main__':
    main()