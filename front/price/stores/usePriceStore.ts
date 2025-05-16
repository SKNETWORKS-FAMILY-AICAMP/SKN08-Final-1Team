import { defineStore } from 'pinia';
import { priceState } from './usePriceState';
import { priceActions } from './usePriceActions';

export const usePriceStore = defineStore('price', {
  state: priceState,
  actions: priceActions
});
