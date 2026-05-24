import DeleteIcon from '@mui/icons-material/Delete';

import "./Icons.css";


interface DeleteIconProps {
	color: string,
	addContainerClassName?: string,
	addClassName?: string,
	onClick?: () => void
}

export function DeleteItemIcon(props: DeleteIconProps) {
	return (
		<div className={ `icon-container ${props.addContainerClassName}` }>
			<div
				className={ `icon ${props.addClassName}` }
				onClick={ props.onClick }
			>
				<DeleteIcon fontSize="medium" sx={{ color: props.color }}/>
			</div>
		</div>
	)
}
