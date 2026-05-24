import "./Tables.css";
import { AddRowIcon } from "../Icons/AddRowIcon";


interface TableAddProps {
	handleOpenWindow: () => void
}

export function TableAdd({ handleOpenWindow }: TableAddProps) {
	return (
		<AddRowIcon
			color="white"
			onClick={ handleOpenWindow }
			addClassName="py-2 px-2 hover:bg-white/10"
			addContainerClassName="basis-1/2"
		/>
	)
}
