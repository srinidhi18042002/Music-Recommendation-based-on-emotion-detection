import streamlit as st 
import spot1
import from_here
# from create import create
# from read import read
# from update import update
# from  delete import  delete
#from database import create_table

def main():
    st.title("Thought I'll tell you joke, but seems like you're too happy already :))))")
    menu = ["I Like Me Better", "Little Things", "They Don't Know About Us", "Make You Mine"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    #create_table()
    if choice == "I Like Me Better":
        
        st.subheader("Listen To I like me better")
        images = ['ilikemebetter.JPG']
        st.image(images, use_column_width=True, caption=["some generic text"] * len(images))
        if st.button("listen"):
            spot1.get_song(choice)
        if st.button("did you *like* like yourself better?"):
            st.subheader("Now that you've liked yourself better, here are a few more songs which will keep the vibe going.")
            lst = list(set(from_here.final(choice)))
            
            for i in lst:
                if st.button(i):
                    spot1.get_song(i)

                

            
                
           
                
                    
                    # spot1.get_song(i)
             #spot1.get_song(choice)
        # elif st.button("see next"):
        #     return
    elif choice == "Little Things":
        st.subheader("Listen To little things")
        images = ['1D.JPG']
        st.image(images, use_column_width=True, caption=["music mania"] * len(images))
        if st.button("listen"):
            spot1.get_song(choice)
        if st.button("like"):
            st.subheader("If little things are what matters to you, here are a little more of our suggestions")
            lst = list(set(from_here.final(choice)))
            
            for i in lst:
                if st.button(i):
                    spot1.get_song(i)
            #return #spot1.get_song(choice)
        # elif st.button("see next"):
        #     return

    elif choice == "They Don't Know About Us":
        st.subheader("Listen To They Don't Know About Us")
        images = ['theydkaboutus.JPG']
        st.image(images, use_column_width=True, caption=["music mania"] * len(images))
        if st.button("listen"):
            spot1.get_song(choice)
        if st.button("like"):
            st.subheader("If 'they dont know' what to listen to next, dont worry we have got 'them' covered")
            lst = list(set(from_here.final(choice)))
            
            for i in lst:
                if st.button(i):
                    spot1.get_song(i)
        # elif st.button("see next"):
        #     return

    elif choice == "Make You Mine":
        st.subheader("Listen To Make You Mine")
        images = ['makeyoumine.JPG']
        st.image(images, use_column_width=True, caption=["music mania"] * len(images))
        if st.button("listen"):
            spot1.get_song(choice)
        if st.button("like"):
            st.subheader("Make this playlist yours ;)")
            lst = list(set(from_here.final(choice)))
            
            for i in lst:
                if st.button(i):
                    spot1.get_song(i)
        
         

    

             


            

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
