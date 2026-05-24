import { IPrivilegeHistory } from "./IPrivilegeHistory"


export interface IPrivilegeResponse {
	balance: number
	status: string
	history: IPrivilegeHistory[]
};
