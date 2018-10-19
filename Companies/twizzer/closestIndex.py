#
# Complete the 'closest' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def closest(s, queries):
    # Write your code here
    indexHash = {}
    closest = []
    for index in range(len(s)):
            if s[index] in indexHash:
                indexHash[s[index]].append(index)
            else:
                indexHash[s[index]] = [index]

    #print(indexHash)


    for query in queries:
        if(query >= len(s)):
            closest.append(-1)
            continue
        #print("checking for index : ", query)
        indexList = indexHash[s[query]]
        #print("indexList: ",indexList)
        index = indexList.index(query)
        closestLeft = -1
        closestRight = - 1
        if index > 0:
            closestLeft = indexList[index - 1]
        if index < len(indexList) - 1:
            closestRight = indexList[index + 1]

        #print("left index: " ,closestLeft , "Right Index: ",closestRight )

        if closestRight == -1 and closestLeft != -1:
            closest.append(closestLeft)
        elif closestRight != -1 and closestLeft == -1:
            closest.append(closestRight)
        elif closestRight == -1 and closestLeft == -1:
            closest.append(-1)
        else:
            if(query - closestLeft <= closestRight - query):
                closest.append(closestLeft)
            else:
                closest.append(closestRight)

        #print("Closed index:  ", closest[-1])


    return closest



def closest(s, queries):

    closest = []
    for query in queries:
        char = s[query]
        print("find char: ", char, "index of char: ", query)
        leftFound = False
        RightFound = False
        leftIndex = query - 1
        rightIndex = query + 1

        # find left
        newList = s[0:leftIndex].reverse()
        leftIndex = s.find(char, 0)

        if(leftIndex != -1):
            leftFound = True
            leftIndex = query - leftIndex
        # while leftIndex != -1:
        #     if char == s[leftIndex]:
        #         leftFound = True
        #         break
        #     leftIndex -= 1

        rightIndex = s.find(char ,query+1)

        if(rightIndex != -1):
            RightFound = True

        print("right: ", rightIndex, "left :",leftIndex)
        if leftFound and RightFound:
            if query - leftIndex <= rightIndex - query:
                closest.append(leftIndex)
            else:
                closest.append(rightIndex)
        elif not leftFound and RightFound:
            closest.append(rightIndex)
        elif  leftFound and not RightFound:
            closest.append(leftIndex)
        else:
            closest.append(-1)


    return closest

    class Result {

    /*
     * Complete the 'closest' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. STRING s
     *  2. INTEGER_ARRAY queries
     */

    public static List<Integer> closest(String s, List<Integer> queries) {
    // Write your code here
        List <Integer> closestList = new ArrayList<>();
        HashMap <Character>  = new HashSet<>();

        for(int i = 0; i < queries.size(); i++){
            set.add(s.charAt(queries.get(i)));
        }

        HashMap<Character,ArrayList<Integer>> map=new HashMap<Character,ArrayList<Integer>>();
        for(int i = 0; i< s.length();i++){
            char target = s.charAt(i);
            if(set.contains(target)){
                if(map.containsKey(target)){
                    (map.get(target)).add(i);
                }else{
                    map.put(target, new ArrayList<Integer>(Collections.singletonList(i)));
                }
            }

        }


        // for (Map.Entry<Character, ArrayList<Integer>> entry : map.entrySet()) {
        // System.out.println(entry.getKey()+" : "+Arrays.toString(entry.getValue().toArray()));
        // }


        for(int i = 0; i < queries.size(); i++){
            int query = queries.get(i);
            char target = s.charAt(query);
            ArrayList<Integer> indexList = map.get(target);
            if(indexList.size() == 1){
                closestList.add(-1);
                continue;
            }
            int index = indexList.indexOf(query);

            boolean leftFound = false;
            boolean rightfound = false;

            //int rightIndex =

            //System.out.println(indexList.size());
            if(index > 0 && index < indexList.size() -1)
                closestList.add(query - indexList.get(index - 1) <= indexList.get(index + 1) - query? indexList.get(index - 1): indexList.get(index + 1));
            else if(index == 0)
                closestList.add(indexList.get(index + 1));
            else if (index == indexList.size() -1)
                closestList.add(indexList.get(index - 1));
        }

        //System.out.println(closestList.get(closestList.size() -1));
        return closestList;
    }

}
