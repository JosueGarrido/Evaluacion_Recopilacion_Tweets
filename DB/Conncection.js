const mongoose = require('mongoose');

const URI ="mongodb+srv://wocking:wockingpro12@twitter-fswc4.mongodb.net/test?retryWrites=true&w=majority";

const connectDB = async () => {
  await mongoose.connect(URI, {
    useUnifiedTopology: true,
    useNewUrlParser: true
  });
  console.log('db connected..!');
};

module.exports = connectDB;
