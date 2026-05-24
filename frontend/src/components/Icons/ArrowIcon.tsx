import ArrowDownwardIcon from '@mui/icons-material/ArrowDownward';
import ArrowUpwardIcon from '@mui/icons-material/ArrowUpward';

import "./Icons.css";


interface ArrowIconProps {
	upward: boolean,
	color: string,
	addContainerClassName?: string,
	addClassName?: string,
	onClick?: () => void
}

export function ArrowIcon(props: ArrowIconProps) {
	return (
		<div className={ `icon-container ${ props.addContainerClassName }` }>
			<div 
				className={ `arrow-icon ${ props.addClassName }` }
				onClick={ props.onClick }
			>
				{ props.upward
					? <ArrowUpwardIcon fontSize='medium' sx={{ color: props.color }}/> 
					: <ArrowDownwardIcon fontSize='medium' sx={{ color: props.color }}/> 
				}
			</div>
		</div>
	)
}
