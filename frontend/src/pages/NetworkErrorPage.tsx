import { TextErrorPage } from '../components/Texts/TextErrorPage';


interface NetworkErrorPageProps {
	openMiniDrawer: boolean
}

export function NetworkErrorPage({ openMiniDrawer }: NetworkErrorPageProps) {
	return (
		<TextErrorPage
			header="Сетевая ошибка"
			text="Не удалось сделать запрос к серверу"
			openMiniDrawer={ openMiniDrawer }
		/>
	)
}
