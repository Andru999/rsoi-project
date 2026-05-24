import NoteAddIcon from '@mui/icons-material/NoteAdd';

import "./Icons.css";


interface AddRowIconProps {
	color: string,
	addContainerClassName?: string,
	addClassName?: string,
	onClick?: () => void
}

export function AddRowIcon(props: AddRowIconProps) {
	return (
		<div className={ `icon-container ${props.addContainerClassName}` }>
			<div
				className={ `icon ${props.addClassName}` }
				onClick={ props.onClick }
			>
				<NoteAddIcon fontSize="medium" sx={{ color: props.color }}/>
			</div>
		</div>
	)
}
