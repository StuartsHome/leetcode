"""Problem :
Given a list of business_names (strings) and a searchTerm (string).
Return a list of business_names that contains searchTerm as prefix in the business_names."""

business_names =  ["burger king", "McDonald's", "super duper burger's", "subway", "pizza hut"]
searchTerm = "bur"

business_names = ["burger king", "McDonald's", "super duper burger's", "subway", "pizza hut"]
searchTerm = "duper bur"
aa = [x.replace(" ","") and x.lower() for x in business_names]
# aa = [x.split() for x in business_names]

# Naive solution 
results = []
for x in aa:
    for word in x:
        word.lower()
        if word.startswith(searchTerm):
            results.append(" ".join(x))
            break
        else:
            results.append(False)
print(results)

def prefix(business_names, searchTerm):
    split = [i.split() for i in business_names]
    ans = []
    for name in split:
        for i in range(len(name)):
            query = ' '.join(name[i:])
            if query.startswith(searchTerm):
                ans.append(name)
                break
    aa = [' '.join(i) for i in ans]
    print(aa)

prefix(business_names, searchTerm)
    