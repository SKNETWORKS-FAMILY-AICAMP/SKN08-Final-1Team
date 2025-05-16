import { defineStore } from 'pinia';
import { adminState } from './adminState';
import { adminAction } from './adminActions';

export const useAdminStore = defineStore('adminStore', {
  state: adminState,
  actions: adminAction,
});