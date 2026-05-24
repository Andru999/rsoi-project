import { Link } from 'react-router-dom';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';


interface DrawerListItemProps {
	openDrawer: boolean
	text: string
	link: string
	icon?: React.ReactNode
	textClassName?: string
}

export function DrawerListItem(props: DrawerListItemProps) {
	return (
		<ListItem 
			disablePadding
			sx={{ display: 'block' }}
			key={ props.text }  
		>
			<Link to={ props.link }>
				<ListItemButton
					sx={{
						minHeight: 48,
						justifyContent: props.openDrawer ? 'initial' : 'center',
						px: 2.5,
					}}
				>
					<ListItemIcon
						sx={{
							minWidth: 0,
							mr: props.openDrawer ? 3 : 'auto',
							justifyContent: 'center',
						}}
					>
						{ props.icon }
					</ListItemIcon>

					<ListItemText 
						primary={
							<p className='text-xl text-gray-600'>
								{ props.text }
							</p>
						}
						sx={{ opacity: props.openDrawer ? 1 : 0 }} 
						className={ props.textClassName }
					/>
				</ListItemButton>
			</Link>
		</ListItem>
	)
}
