# Connect to SharePoint
Connect-PnPOnline -Url "https://thetaco1nz.sharepoint.com/sites/Sudeep" -UseWebLogin

# Create list
New-PnPList -Title "Popular Books" -Template GenericList -Url "Lists/PopularBooks" -OnQuickLaunch

# Add columns (as per requirements)

Add-PnPField -List "Popular Books" -DisplayName "Number" -InternalName "Number" -Type Number
Add-PnPField -List "Popular Books" -DisplayName "BookAuthor" -InternalName "BookAuthor" -Type Text
Add-PnPField -List "Popular Books" -DisplayName "BookAbstract" -InternalName "BookAbstract" -Type Note
Add-PnPField -List "Popular Books" -DisplayName "Category" -InternalName "Category" -Type Text
Add-PnPField -List "Popular Books" -DisplayName "Price" -InternalName "Price" -Type Text
Add-PnPField -List "Popular Books" -DisplayName "BookCoverUrl" -InternalName "BookCoverUrl" -Type Text
Add-PnPField -List "Popular Books" -DisplayName "IsBestSeller" -InternalName "IsBestSeller" -Type Boolean
Add-PnPField -List "Popular Books" -DisplayName "ReleaseDate" -InternalName "ReleaseDate" -Type DateTime
Add-PnPField -List "Popular Books" -DisplayName "FindInStoreUrl" -InternalName "FindInStoreUrl" -Type Text
Add-PnPField -List "Popular Books" -DisplayName "AddToCart" -InternalName "AddToCart" -Type Boolean

# Insert sample book records
Add-PnPListItem -List "Popular Books" -Values @{ Number = "1"; BookAuthor = "J.K. Rowling"; Title = "Harry Potter"; Category = "Fantasy"; Price = "39.99"; BookAbstract = "Harry discovers he is a wizard and attends Hogwarts, where he makes friends and faces the dark wizard Voldemort."; BookCoverUrl = "https://images-na.ssl-images-amazon.com/images/I/81YOuOGFCJL.jpg"; IsBestSeller = $true; ReleaseDate = "1997-06-26"; FindInStoreUrl = "https://www.google.com/maps?q=amazon+books+store+nyc"; AddToCart = $false }
Add-PnPListItem -List "Popular Books" -Values @{ Number = "2"; BookAuthor = "J.R.R. Tolkien"; Title = "The Lord of the Rings"; Category = "Fantasy"; Price = "59.99"; BookAbstract = "Frodo Baggins embarks on a perilous journey to destroy the One Ring and save Middle-earth from Sauron."; BookCoverUrl = "https://images-na.ssl-images-amazon.com/images/I/91SZSW8qSsL.jpg"; IsBestSeller = $true; ReleaseDate = "1954-07-29"; FindInStoreUrl = "https://www.google.com/maps?q=amazon+books+store+nyc"; AddToCart = $false }
Add-PnPListItem -List "Popular Books" -Values @{ Number = "3"; BookAuthor = "George Orwell"; Title = "1984"; Category = "Dystopian"; Price = "24.50"; BookAbstract = "Winston Smith rebels against a totalitarian regime that watches every move and controls every thought."; BookCoverUrl = "https://images-na.ssl-images-amazon.com/images/I/71kxa1-0mfL.jpg"; IsBestSeller = $false; ReleaseDate = "1949-06-08"; FindInStoreUrl = "https://www.google.com/maps?q=amazon+books+store+nyc"; AddToCart = $false }
Add-PnPListItem -List "Popular Books" -Values @{ Number = "4"; BookAuthor = "Jane Austen"; Title = "Pride and Prejudice"; Category = "Classic"; Price = "29.95"; BookAbstract = "Elizabeth Bennet navigates issues of manners, upbringing, and marriage in 19th-century England."; BookCoverUrl = "https://images-na.ssl-images-amazon.com/images/I/81OthjkJBuL.jpg"; IsBestSeller = $false; ReleaseDate = "1813-01-28"; FindInStoreUrl = "https://www.google.com/maps?q=amazon+books+store+nyc"; AddToCart = $false }
Add-PnPListItem -List "Popular Books" -Values @{ Number = "5"; BookAuthor = "F. Scott Fitzgerald"; Title = "The Great Gatsby"; Category = "Classic"; Price = "44.00"; BookAbstract = "Jay Gatsby pursues wealth and love in the Roaring Twenties, only to face tragedy and disillusionment."; BookCoverUrl = "https://images-na.ssl-images-amazon.com/images/I/81af+MCATTL.jpg"; IsBestSeller = $true; ReleaseDate = "1925-04-10"; FindInStoreUrl = "https://www.google.com/maps?q=amazon+books+store+nyc"; AddToCart = $false }
Add-PnPListItem -List "Popular Books" -Values @{ Number = "6"; BookAuthor = "Yuval Noah Harari"; Title = "Sapiens"; Category = "Non-Fiction"; Price = "54.25"; BookAbstract = "A thought-provoking exploration of humanity's history, from ancient ancestors to the modern world."; BookCoverUrl = "https://images-na.ssl-images-amazon.com/images/I/713jIoMO3UL.jpg"; IsBestSeller = $false; ReleaseDate = "2011-01-01"; FindInStoreUrl = "https://www.google.com/maps?q=amazon+books+store+nyc"; AddToCart = $false }
