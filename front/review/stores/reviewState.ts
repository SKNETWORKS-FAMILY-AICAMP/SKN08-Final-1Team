export const reviewState = () => ({
  reviewTitleList: [] as string[],
  reviewForm: null as Review | null,
  resultForm: null as Review | null,
});

export type Review = {
  reviewId: number;
  reviewTitle: string;
  reviewDescription: string;
  reviewQuestions: any[];
  randomString: string;
};
