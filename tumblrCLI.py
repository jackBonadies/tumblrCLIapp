import pytumblr
 
# Authenticate via API Key
# Make the request
#print (client.posts('staff', limit=2, offset=0, filter='html'))


def defaultConnect():
#client = !!!
	return client

def listPostsFrom(client, num):
	print("starting")
	f = open("allPostsFinal.txt", "a") #remove
	dictionaryOfPosts = client.posts("7fortress",filter='text',limit='20',offset=num)
	listOfPostsWithExtras = dictionaryOfPosts['posts']
	strippedPosts =[]
	for postDict in listOfPostsWithExtras:
		try:
			if(postDict['type']!='text'):
				continue #get rid of photo posts
			if('source_url' in postDict):
				continue #get rid of reblogs
			strippedPosts.append(postDict['body'])
		except:
			continue
	for post in strippedPosts:
		s = str(post)
		f.write(s)
		f.write('\n----------------\n')
		print(s)
	f.flush()

def grabAllTextPosts(client):
	offset = 0
	while(offset<600):
		listPostsFrom(client,offset)
		offset+=20

def console():
	client = defaultConnect()
	print("Welcome to the tumblr CLI app\n")
	print("-----------------------------\n")
	lines = []
	while(1):
		print("new post: ")
		while True:
			line = input()
			if line:
				lines.append(line)
			else:
				break
		text = '\n'.join(lines)	
		print("----post-successful----")
		client.create_text("7fortress.tumblr.com",body=text)
		print(text)
		print("----^^^^^^^^^^^^^^^----\n\n")

def printLatestPosts():
        client = defaultConnect()
        dictionaryOfPosts = client.posts("7fortress",filter='text',limit='20')
        listOfPostsWithExtras = dictionaryOfPosts['posts']
        strippedPosts =[]
        for postDict in listOfPostsWithExtras:
                try:
                        if(postDict['type']!='text'):
                                continue #get rid of photo posts
                        if('source_url' in postDict):
                                continue #get rid of reblogs
                        strippedPosts.append(postDict['body'])
                except:
                        continue
        for post in strippedPosts:
                s = str(post)
                print(s)

#console()
printLatestPosts()
