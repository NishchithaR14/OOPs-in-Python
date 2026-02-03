# Class and object

class Instagram:
    def __init__(self,title, description,creator_name,location):    
        self.title = title
        self.description = description
        self.likes = 0
        self.creator_name = creator_name 
        self.location = location
        self.comments = []
        
    def display_title(self):
        print("The title of the reel is ",self.title)

    def display_description(self):
        print("The description of the reel is ",self.description)

    def display_likes(self):
        print("The likes of the reel is ",self.likes)

    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes-=1 

    def display_creator_name(self):
        print("The creator name is ",self.creator_name) 

    def display_location(self):
        print("The location is ",self.location)

    def display_comment(self):
        if len(self.comments) == 0:
            print("No comments yet")
        else:
            print("The comments are ")
            for comment in self.comments: 
                print("-",comment)

    def add_comments(self,comment):
        self.comments.append(comment)

    def delete_last_comment(self):
        temp_comment=self.comments.pop()
        print("The last comment is deleted ",temp_comment)



reel1=Instagram("dancing","dancing with friends","Nishchitha","Mysore")

reel1.liked()
reel1.liked()

reel1.display_title()
reel1.display_description()
reel1.display_creator_name()
reel1.display_location()
reel1.add_comments("Awesome")
reel1.display_comment()
reel1.delete_last_comment()
reel1.display_comment()




reel2=Instagram("finance minister conference","finance minister conference with friends","ABC","Delhi") 
reel2.liked()
reel2.liked()

reel2.display_title()
reel2.display_description()
reel2.display_creator_name()
reel2.display_location()
reel2.add_comments("Good")
reel2.display_comment()
reel2.delete_last_comment()
reel2.display_comment()

print(id(reel1))
print(id(reel2))
