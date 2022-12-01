import streamlit as st 
import spot1
import from_here
def main():
    st.title("Aww, who broke your heart? :/")
    menu = ["Little Do You Know", "all the kids are depressed", "Be Alright"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Little Do You Know":
        
        st.subheader("Listen To Little Do You Know")
        if st.button("listen"):
            images = ['lildouknow.JPG']
            st.image(images, use_column_width=True, caption=["music mania"] * len(images))
            spot1.get_song(choice)
        if st.button("like"):
            st.subheader("We sure know the kind of songs you'd wanna hear rn :/")
            lst = list(set(from_here.final(choice)))
            
            for i in lst:
                if st.button(i):
                    spot1.get_song(i)

                

            
                
           
                
                    
                    # spot1.get_song(i)
             #spot1.get_song(choice)
        # elif st.button("see next"):
        #     return
    elif choice == "all the kids are depressed":
        st.subheader("Listen To all the kids are depressed")
        images = ['allthekis.JPG']
        st.image(images, use_column_width=True, caption=["some generic text"] * len(images))
        if st.button("listen"):
            spot1.get_song(choice)
        if st.button("like"):
            st.subheader("Now that you have liked it, here you go")
            lst = list(set(from_here.final(choice)))
            
            for i in lst:
                if st.button(i):
                    spot1.get_song(i)
            #return #spot1.get_song(choice)
        # elif st.button("see next"):
        #     return

    elif choice == "Be Alright":
        st.subheader("Listen To Be Alright")
        images = ['bealright.JPG']
        st.image(images, use_column_width=True, caption=["some generic text"] * len(images))
        if st.button("listen"):
            spot1.get_song(choice)
        if st.button("like"):
            st.subheader("You'll be alright mate, follow our tracks")
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