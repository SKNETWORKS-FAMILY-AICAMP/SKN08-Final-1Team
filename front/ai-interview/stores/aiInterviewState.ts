export const aiInterviewState = () => ({
    userInput: "",
  
    // 면접 관련 상태
    interviewId: null as number | null,
    questionId: null as number | null,
    question: "" as string,
    answer: "" as string,
  
    // 질문/답변 전체 리스트 
    questionList: [] as string[],
    answerList: [] as string[],
  
    // context (회사, 직무 등)
    context: {
      company: "",
      position: "",
      level: "",
      project: "",
      tech: ""
    }
  });
  