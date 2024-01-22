


#CS306 PROJECT PHASE4
import certifi
from bson import ObjectId



#Dummy data to check while inserting data
dummy_data = [
    {"Title": "Inception", "ReleaseDate": "2010-07-16", "Genre": "Sci-Fi", "Runtime": 150},
    {"Title": "The Shawshank Redemption", "ReleaseDate": "1994-09-23", "Genre": "Drama", "Runtime": 150},
    {"Title": "The Dark Knight", "ReleaseDate": "2008-07-18", "Genre": "Action", "Runtime": 150},
    {"Title": "Pulp Fiction", "ReleaseDate": "1994-10-14", "Genre": "Crime", "Runtime": 150},
    {"Title": "Forrest Gump", "ReleaseDate": "1994-07-06", "Genre": "Drama", "Runtime": 142},
    {"Title": "The Matrix", "ReleaseDate": "1999-03-31", "Genre": "Sci-Fi", "Runtime": 136},
    {"Title": "Titanic", "ReleaseDate": "1997-12-19", "Genre": "Romance", "Runtime": 195},
    {"Title": "The Godfather", "ReleaseDate": "1972-03-24", "Genre": "Crime", "Runtime": 175},
    {"Title": "Avatar", "ReleaseDate": "2009-12-18", "Genre": "Action", "Runtime": 162},
    {"Title": "Jurassic Park", "ReleaseDate": "1993-06-11", "Genre": "Adventure", "Runtime": 127},
]

dummy_crew_data = [
    {"Crew_Member_Name": "John Smith", "Crew_Member_Role": "Director", "Film_id": 1},
    {"Crew_Member_Name": "Jane Johnson", "Crew_Member_Role": "Producer", "Film_id": 2},
    {"Crew_Member_Name": "Robert Davis", "Crew_Member_Role": "Cinematographer", "Film_id": 3},
    {"Crew_Member_Name": "Alice White", "Crew_Member_Role": "Editor", "Film_id": 4},
    {"Crew_Member_Name": "Michael Brown", "Crew_Member_Role": "Screenwriter", "Film_id": 5},
    {"Crew_Member_Name": "Emily Miller", "Crew_Member_Role": "Production Designer", "Film_id": 6},
    {"Crew_Member_Name": "Daniel Lee", "Crew_Member_Role": "Editor", "Film_id": 7},
    {"Crew_Member_Name": "Olivia Robinson", "Crew_Member_Role": "Sound Designer", "Film_id": 8},
    {"Crew_Member_Name": "Andrew Wilson", "Crew_Member_Role": "Editor", "Film_id": 9},
    {"Crew_Member_Name": "Sophia Taylor", "Crew_Member_Role": "Makeup Artist", "Film_id": 10},
]




from pymongo import MongoClient

# First of all, install the pymongo using pip
# python -m pip install "pymongo[srv]"
def connectDB():
    # Replace the connection string with your MongoDB connection string
    # You can obtain the connection string from your MongoDB Atlas dashboard or configure it locally
    # For example, if your database is running on localhost, the connection string might look like this:
    # "mongodb://localhost:27017/"

    connection_string = "mongodb+srv://admin:passw@atlascluster.aga9c3l.mongodb.net/?ssl=true&retryWrites=true&w=majority"
    client = MongoClient(connection_string,tlsCAFile=certifi.where()) #this one added later after error

    # Access a specific database (replace "your_database_name" with your actual database name)
    db = client.AtlasCluster
    print("Connection established to your db")
    return db
    # Close the connection when you're done
    # client.close()
    
    
from pymongo import errors


def createCollection(db, collection_name):
    try:
        # If the collection doesn't exist, create it
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Collection '{collection_name}' created.")
        elif collection_name in db.list_collection_names():
            print("Collection already exists")
    except Exception as e:
        print("An error occured: ", e)
        
        
        
def insert_into_collection(db, collection_name, data):
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Insert the data into the collection
        result = collection.insert_one(data)

        # Print the inserted document ID
        print("Insertion successfully completed")
        print(f"Inserted document ID: {result.inserted_id}")

    except Exception as e:
        print(f"An error occurred: {e}")
        
def read_all_data(db, collection_name):
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Use the find method to retrieve all documents
        result = collection.find()

        # Iterate through the documents and print them
        for document in result:
            print(document)

    except Exception as e:
        print(f"An error occurred: {e}")



def find_film_containing_item(db, collection_name, Runtime):
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Define the query to find orders containing the specified item
        query = {"Runtime": Runtime}

        # Use the find method to retrieve matching documents
        cursor = collection.find(query)

        # Convert your cursor to a list to freely operate over it
        result = list(cursor)

        # Print the matching documents
        for document in result:
            print(document)

        # Return the whole result list
        return result

    except Exception as e:
        print(f"An error occurred: {e}")


def find_crew_containing_item(db, collection_name, Crew_Member_Role):
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Define the query to find orders containing the specified item
        query = {"Crew_Member_Role": Crew_Member_Role}

        # Use the find method to retrieve matching documents
        cursor = collection.find(query)

        # Convert your cursor to a list to freely operate over it
        result = list(cursor)

        # Print the matching documents
        for document in result:
            print(document)

        # Return the whole result list
        return result

    except Exception as e:
        print(f"An error occurred: {e}")


def delete_record_by_id(db, collection_name, record_id):
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Define the query to find the document by its ID
        query = {"_id": record_id}

        # Use the delete_one method to delete the document
        result = collection.delete_one(query)

        # Check if the deletion was successful
        if result.deleted_count == 1:
            print(f"Successfully deleted record with ID {record_id}")
        else:
            print(f"No record found with ID {record_id}")

    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")



def update_crew_list_by_id(db, collection_name, record_id, new_crew_list):
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Define the query to find the document by its ID
        query = {"_id": record_id}

        # Use the update_one method to update the specific field (order_list)
        result = collection.update_one(query, {"$set": {"Crew_Member_Role": new_crew_list}})

        # Check if the update was successful
        if result.matched_count == 1:
            print(f"Successfully updated order_list for record with ID {record_id}")
        else:
            print(f"No record found with ID {record_id}")

    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")



def update_film_list_by_id(db, collection_name, record_id, new_film_list):
    try:
        # Access the specified collection
        collection = db[collection_name]

        # Define the query to find the document by its ID
        query = {"_id": record_id}

        # Use the update_one method to update the specific field (order_list)
        result = collection.update_one(query, {"$set": {"Runtime": new_film_list}})

        # Check if the update was successful
        if result.matched_count == 1:
            print(f"Successfully updated order_list for record with ID {record_id}")
        else:
            print(f"No record found with ID {record_id}")

    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # First create a connection
    db = connectDB()

    
    
    def user_interface():
        
        
        print("Welcome to Review Portal!")
        user_id = input("Please enter your user id: ")
        review_collection = None
    
        while True:
            

            print("Please pick the option that you want to proceed:")
            print("1- Create a collection.")
            print("2- Read all data in a collection.")
            print("3- Read some part of the data while filtering.")
            print("4- Insert data.")
            print("5- Delete data.")
            print("6- Update data.")
            
            selected_option = input("Selected option: ")
            
            if selected_option == '1':
                collection_name = input("Enter collection name: ")
                review_collection = collection_name
                createCollection(db, collection_name)               
                
            elif selected_option == '2':
                if review_collection is None:
                    print("Please create or select a collection first.")
                else:
                    print("Please select the collection to read:")
                    print("1-Films")
                    print("2-CrewMembers")
                    
                    read_option = input("Selected option:")
                    
                    if(read_option == '1'):
                        review_collection = "Films"
                        read_all_data(db,review_collection)
                    elif(read_option == '2'):
                        review_collection = "CrewMembers"
                        read_all_data(db,review_collection)
                
            elif selected_option == '3':
                if review_collection is None:
                    print("Please create or select a collection first.")
                else:
                    print("Please select the filtering option:")
                    print("1- Find by Runtime")
                    print("2- Find by Crew Member Role")

                    filter_option = input("Selected option: ")

                    if filter_option == '1':
                        review_collection = "Films"
                        Runtime = input("Enter Runtime: ")
                        find_film_containing_item(db,review_collection,Runtime)

                    elif filter_option == '2':
                        review_collection = "CrewMembers"
                        Crew_Member_Role = input("Enter Crew Member Role: ")
                        find_crew_containing_item(db,review_collection,Crew_Member_Role)
                    
            elif selected_option == '4':
                if review_collection is None:
                    print("Please create a collection first.")
                else:
                    print("Please select the collection you want to insert data:")
                    print("1-Films")
                    print("2-CrewMembers")

                    insert_option = input("Selected option: ")

                    if insert_option == '1':
                        review_collection = "Films"
                        print("Please enter the data fields:")
                        Title = input("Title: ")
                        ReleaseDate = input("ReleaseDate (YYYY-MM-DD): ")
                        Genre = input("Genre: ")
                        Runtime = input("Runtime: ")
                        
                        film_data = {
                            "Title": Title,
                            "ReleaseDate": ReleaseDate,
                            "Genre": Genre,
                            "Runtime": Runtime,
                        }
                        insert_into_collection(db,review_collection,film_data)


                    elif insert_option == '2':
                        review_collection = "CrewMembers"
                        print("Please enter the data fields:")
                        
                        Crew_Member_Name = input("Crew Member Name: ")
                        Crew_Member_Role = input("Crew Member Role: ")
                        Film_id = input("Film ID: ")

                        crew_member_data = {
                            "Crew_Member_Name": Crew_Member_Name,
                            "Crew_Member_Role": Crew_Member_Role,
                            "Film_id": Film_id,
                        
                        }
            
                        insert_into_collection(db,review_collection,crew_member_data)
            
            elif(selected_option == '5'):
                
                
                if review_collection is None:
                    print("Please create or select a collection first.")
                else:
           
                    print("Please select the collection you want to delete data from:")
                    print("1-Films")
                    print("2-CrewMembers")

                    delete_option = input("Selected option: ")

                    if delete_option == '1':
                        review_collection = "Films"
                        print("Deleting data from Films")
                        record_id = input("Enter the ID of the record to delete: ")
                        record_id = ObjectId(record_id)

                        delete_record_by_id(db,review_collection,record_id)

                    elif delete_option == '2':
                        review_collection = "CrewMembers"
                        print("Deleting data from CrewMembers")
                        record_id = input("Enter the ID of the record to delete: ")
                        record_id = ObjectId(record_id)
                        
                        delete_record_by_id(db, review_collection,record_id)
                             

            elif selected_option == '6':
                if review_collection is None:
                    print("Please create or select a collection first.")
                else:
           
                    print("Please select the collection you want to update data in:")
                    print("1-Films")
                    print("2-CrewMembers")

                    update_option = input("Selected option: ")

                    if update_option == '1':
                        review_collection = "Films"
                        print("Updating data in Films")                       
                        record_id = input("Enter the ID of the record to update: ")
                        record_id = ObjectId(record_id)                       
                        new_runtime = input("Enter the new Runtime value: ")                      
                        update_film_list_by_id(db, review_collection,record_id, new_runtime)
                    
                    elif update_option == '2':
                        review_collection = "CrewMembers"
                        print("Updating data in CrewMembers Collection")             
                        record_id = input("Enter the ID of the record to update: ")    
                        record_id = ObjectId(record_id)
                        new_crew_list = input("Enter the new Crew Member Role value: ")               
                        update_crew_list_by_id(db, review_collection, record_id, new_crew_list)
                

    user_interface()
    
    
