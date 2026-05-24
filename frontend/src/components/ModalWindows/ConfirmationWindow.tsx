import "./ModalWindows.css";
import { Backdrop } from "./Backdrop";
import { TextHeader } from "../Texts/TextHeader";
import { ConfirmIcon } from "../Icons/ConfirmIcon";
import { RejectIcon } from "../Icons/RejectIcon";


interface ConfirmationWindowProps {
	header: string,
	children?: any,
	onClose: () => void,
	onConfirm: () => void
}

export function ConfirmationWindow({ header, children, onClose, onConfirm }: ConfirmationWindowProps) {
	return (
		<>
			<Backdrop onClick={ onClose }/>

			<div className="confirmation-window">
				<TextHeader text={ header }/>

				{ children }

				<div className="right-buttons">
					<ConfirmIcon
						color="white"
						onClick={ onConfirm }
						addClassName="px-8 py-2"
						addContainerClassName="mr-2"
					/>
					<RejectIcon
						color="#197aca"
						onClick={ onClose }
						addClassName="px-8 py-2"
						addContainerClassName="w-24"
					/>
				</div>
			</div>
		</>
	)
}
