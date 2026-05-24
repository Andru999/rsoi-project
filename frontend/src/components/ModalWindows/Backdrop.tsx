import "./ModalWindows.css";


interface BackdropProps {
	onClick: () => void
}

export function Backdrop({ onClick }: BackdropProps) {
	return (
		<div className="backdrop" onClick={ onClick }/>
	)
}
