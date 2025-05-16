export const priceState = () => ({
    pricePlans: [] as {
      id: number;
      name: string;
      price: string;
      originalPrice?: string;
      period: string;
      features: string[];
    }[]
  });
  