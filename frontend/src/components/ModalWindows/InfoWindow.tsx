import "./ModalWindows.css";
import { Backdrop } from "./Backdrop";
import { FormButton } from "../Buttons/FormButton";
import { TextHeader } from "../Texts/TextHeader";
import { TextField } from "../Texts/TextField";


interface InfoWindowProps {
	header: string,
	text: string,
	onClose: () => void
}

export function InfoWindow({ header, text, onClose }: InfoWindowProps) {
	return (
		<>
			<Backdrop onClick={ onClose }/>

			<div className="info-window">
				<TextHeader text={ header }/>
				<TextField text={ text }/>

				<div className="right-buttons">
					<FormButton 
						text="Ок"
						onClick={ onClose }
					/>
				</div>
			</div>
		</>
	)
}
