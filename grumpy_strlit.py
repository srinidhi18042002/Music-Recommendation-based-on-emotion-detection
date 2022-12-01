import streamlit as st 
import spot1
import from_here
def main():
    st.title("Heyy, Need an outlet to remove all your frustration? Rap along!!")
    menu = ["Kamikaze", "Venom", "Remember the Name (feat. Styles of Beyond)"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Kamikaze":
        
        st.subheader("Listen To Kamikaze")
        if st.button("listen"):
            spot1.get_song(choice)
        if st.button("like"):
            st.subheader("Eminem fan? Listen to more hits")
            lst = list(set(from_here.final(choice)))
            
            for i in lst:
                if st.button(i):
                    spot1.get_song(i)

                

            
                
           
                
                    
                    # spot1.get_song(i)
             #spot1.get_song(choice)
        # elif st.button("see next"):
        #     return
    elif choice == "Venom":
        st.subheader("Listen To Venom")
        if st.button("listen"):
            spot1.get_song(choice)
        if st.button("like"):
            st.subheader("Need some gym motivation? Grab your earphones")
            lst = list(set(from_here.final(choice)))
            
            for i in lst:
                if st.button(i):
                    spot1.get_song(i)
            #return #spot1.get_song(choice)
        # elif st.button("see next"):
        #     return

    elif choice == "Remember the Name (feat. Styles of Beyond)":
        st.subheader("Listen To Remember the Name (feat. Styles of Beyond)")
        if st.button("listen"):
            spot1.get_song(choice)
        if st.button("like"):
            st.subheader("They say music is the best outlet. Mind trying?")
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