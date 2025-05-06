// backend/routes/product.js
import { Router } from 'express';
import { find } from '../models/Product';
const router = Router();

router.get('/', async (req, res) => {
  const products = await find();
  res.json(products);
});

// Additional routes for creating, updating, deleting products can go here

export default router;
