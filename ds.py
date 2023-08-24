import os

# Đường dẫn thư mục cha
parent_directory = 'D:\\Code\\JS\\Udemy'

# Tên các thư mục con
folders = [ "22 Backend Web Development",
    "23 Node.js",
    "24 Express.js with Node.js",
    "25 APIs - Application Progaming Interface",
    "26 Git, Github, Version Control",
    "27 EJS",
    "28 Boss Level Chanllenges 3 - Blog Website",
    "29 Databases",
    "30 SQL",
    "31 MongoDB",
    "32 Mongoose",
    "33 Putting Everything Together",
    "34 Deloying Your Web Application",
    "36 Build Your Own RestfulAPI from Scratch",
    "37 Authentication & Security",
    "38 React.js",
    "39 Web 3 Decentralised App (Dapp) Development with the internet computer",
    "40 Build Your First Defi (Decentralised Finance ) Dapp - Dbank",
    "41 Deploying ti the ICP live Blockchain",
    "42 Building Dapps on ICP with a React Fontend",
    "43 Create Your Own Crypto Token",
    "44 Minting NFTs and Building an NFT Maketplace like OpenSea",
    "45 Optional Module Ask Agela Anything"]

# Lặp qua danh sách tên thư mục và tạo từng thư mục
for folder in folders:
    # Đường dẫn đầy đủ đến thư mục con
    path = os.path.join(parent_directory, folder)
    
    # Kiểm tra xem thư mục đã tồn tại hay chưa
    if not os.path.exists(path):
        # Tạo thư mục mới nếu chưa tồn tại
        os.makedirs(path)
        print(f'Thư mục {folder} đã được tạo.')
    else:
        print(f'Thư mục {folder} đã tồn tại.')
