package request_form

type WorkflowTriggerRequestForm struct {
	Token       string `json:"userToken"`
	RepoUrl     string `json:"repoUrl"`
	WorkflowName string `json:"workflowName"`
}