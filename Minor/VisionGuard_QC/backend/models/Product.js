// backend/models/Product.js
import { Schema, model } from 'mongoose';

const ProductSchema = new Schema({
  name: String,
  expiryDate: Date,
  brand: String,
  count: Number,
  freshness: String,  // e.g., "Fresh", "Spoiled"
});

export default model('Product', ProductSchema);
