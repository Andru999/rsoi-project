import FilterListIcon from '@mui/icons-material/FilterList';
import FilterListOffIcon from '@mui/icons-material/FilterListOff';

import "./Icons.css";


interface FilterIconProps {
	color: string,
	selected: boolean,
	addContainerClassName?: string,
	addClassName?: string,
	onClick?: () => void
}

export function FilterIcon(props: FilterIconProps) {
	return (
		<div className={ `icon-container ${ props.addContainerClassName }` }>
			<div 
				className={ `icon ${ props.addClassName }` } 
				onClick={ props.onClick }
			>
				{ props.selected
					? <FilterListIcon fontSize="medium" sx={{ color: props.color }}/> 
					: <FilterListOffIcon fontSize="medium" sx={{ color: props.color }}/> 
				}
			</div>
		</div>
	)
}
