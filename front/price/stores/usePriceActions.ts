export const priceActions = {
    fetchPricePlans() {
      console.log('📦 priceActions.fetchPricePlans() 호출됨');
  
      this.pricePlans = [
        {
          id: 1,
          name: '하루 요금제',
          price: '4000',
          period: '1일',
          features: ['기본 면접 질문 제공', 'AI 모의 면접 1일 무제한', '채용 정보 제공'],
        },
        {
          id: 2,
          name: '일주일 요금제',
          price: '20000',
          originalPrice: '28000',
          period: '1주',
          features: ['기본 면접 질문 제공', 'AI 모의 면접 1주 무제한', '채용 정보 제공'],
        },
        {
          id: 3,
          name: '한달 요금제',
          price: '60000',
          originalPrice: '80000',
          period: '1달',
          features: ['기본 면접 질문 제공', 'AI 모의 면접 1달 무제한', '채용 정보 제공'],
        },
      ];
    }
  };
  