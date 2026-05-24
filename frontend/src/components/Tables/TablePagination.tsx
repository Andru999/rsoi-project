import MuiTablePagination from '@mui/material/TablePagination';

import "./Tables.css";


interface TablePaginationProps {
	amountItems: number,
	page: number,
	rowsPerPage: number,
	handleChangePage: (event: React.MouseEvent<HTMLButtonElement> | null, newPage: number) => void,
	handleChangeRowsPerPage: (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => void
}

export function TablePagination(props: TablePaginationProps) {
	return (
		<div className="pagination">
			<MuiTablePagination
				component="div"
				count={ props.amountItems }
				page={ props.page }
				onPageChange={ props.handleChangePage }
				rowsPerPage={ props.rowsPerPage }
				onRowsPerPageChange={ props.handleChangeRowsPerPage }
				rowsPerPageOptions={ [20, 50, 100] }
				showFirstButton={ true }
				showLastButton={ true }
				labelRowsPerPage={
					<span className="text-xl"> 
						Строк на странице:
					</span>
				}
				labelDisplayedRows={
					({ from, to, count }) => { 
						return (
							<span className="text-xl"> 
								{ `${from}-${to} из ${count}` } 
							</span>
						)
					}
				}
				sx={{ 
					marginX: "auto",
					fontSize: "1.25rem",
					color: "#4b5563"
				}}
			/>
		</div>
	)
}
